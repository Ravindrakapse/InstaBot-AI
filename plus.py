import random
from ollama import chat
import re
import torch
from diffusers import FluxPipeline
from instagrapi import Client
import os


###################### Prompt and Caption Generation: Deepseek ##############
def clean_text(text):
    """Clean the extracted text by removing extra whitespace and unwanted characters"""
    if text:
        # Remove extra whitespace and newlines
        text = ' '.join(text.split())
        # Remove hashtags if they appear at the end of caption
        text = re.sub(r'\s+#\w+(?:\s*,\s*#\w+)*\s*$', '', text)
        return text.strip()
    return None

def extract_content(text):
    """Extract image prompt and caption using multiple patterns"""
    # Remove the <think> sections first
    text = re.sub(r'<think>.*?</think>', '', text, flags=re.DOTALL)
    
    # List of possible patterns for image prompt
    prompt_patterns = [
        r'\*\*[Ii]mage[_ ]?[Pp]rompt:?\*\*\s*"?([^"]+)"?(?=\n|$)',
        r'\*\*[Ii]mage[_ ]?[Pp]rompt:?\*\*\s*(.+?)(?=\n\n|\*\*|$)',
        r'[Ii]mage[_ ]?[Pp]rompt:?\s*"?([^"]+)"?(?=\n|$)',
        r'[Ii]mage[_ ]?[Pp]rompt:?\s*(.+?)(?=\n\n|\*\*|$)'
    ]
    
    # List of possible patterns for image caption
    caption_patterns = [
        r'\*\*[Ii]mage[_ ]?[Cc]aption:?\*\*\s*"?([^"]+)"?(?=\n|$)',
        r'\*\*[Ii]mage[_ ]?[Cc]aption:?\*\*\s*(.+?)(?=\n\n|\*\*|$)',
        r'[Ii]mage[_ ]?[Cc]aption:?\s*"?([^"]+)"?(?=\n|$)',
        r'[Ii]mage[_ ]?[Cc]aption:?\s*(.+?)(?=\n\n|\*\*|$)'
    ]
    
    # Try each prompt pattern until one works
    image_prompt = None
    for pattern in prompt_patterns:
        match = re.search(pattern, text, re.DOTALL)
        if match:
            image_prompt = clean_text(match.group(1))
            break
    
    # Try each caption pattern until one works
    image_caption = None
    for pattern in caption_patterns:
        match = re.search(pattern, text, re.DOTALL)
        if match:
            image_caption = clean_text(match.group(1))
            break
    
    return image_prompt, image_caption


def generate_prompt_caption(characters,activities,settings):

    # Randomly select elements
    character = random.choice(characters)
    activity = random.choice(activities)
    setting = random.choice(settings)

    # Generate prompt using DeepSeek R1
    response = chat(model='deepseek-r1:7b', messages=[{
        'role': 'user',
        'content': f'Write a funny scenario involving {character} from Breaking Bad doing {activity} in {setting}. Make it to generate an image (I want a prompt to generate an image), write in this specific format (image_prompt: , image_caption: , add hashtag in image_caption) dont write another format. Keep it under 50 words.'
    }])

    # Extract the content from the response
    content = response['message'].content
    print("Generated content:")
    # Extract prompt and caption
    image_prompt, image_caption = extract_content(content)

    # Print results with error checking
    print("\nImage Prompt:")
    print(image_prompt if image_prompt else "Could not extract image prompt")
    print("\nImage Caption:")
    print(image_caption if image_caption else "Could not extract image caption")

    return image_prompt, image_caption

###################### Post to Instagram ##############

def post_to_instagram(image_path, caption):
    """Post image to Instagram"""
    try:
        # Initialize Instagram client
        cl = Client()
        cl.load_settings("session.json")
        
        # Upload photo
        media = cl.photo_upload(image_path, caption)
        print("Post uploaded successfully to Instagram!")
        return True
    except Exception as e:
        print(f"Error posting to Instagram: {str(e)}")
        return False

###################### Image Generation: FLUX ##############

def generate_image(prompt, caption, output_dir="out"):
    """Generate image using Flux pipeline"""
    try:
        seed = random.randint(0, 2**32 - 1)
        # Create output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)
        
        # Initialize the pipeline
        pipe = FluxPipeline.from_pretrained("black-forest-labs/FLUX.1-dev", torch_dtype=torch.bfloat16)
        pipe.enable_model_cpu_offload()
        
        # Generate the image
        image = pipe(
            prompt,
            height=1024*2,
            width=1024*2,
            guidance_scale=3.5,
            num_inference_steps=50,
            max_sequence_length=512,
            generator=torch.Generator("cuda").manual_seed(seed)
        ).images[0]
        
        # Save the image
        output_path = f"{output_dir}/Creative_bb_{seed}.png"
        image.save(output_path)
        print(f"Image saved to: {output_path}")
        
        # Post to Instagram
        if post_to_instagram(output_path, caption):
            print("Successfully posted to Instagram")
        else:
            print("Failed to post to Instagram")
        
        # Clean up the image file
        os.remove(output_path)
        print(f"Cleaned up temporary image file: {output_path}")
        
        return True
    except Exception as e:
        print(f"Error generating image: {str(e)}")
        return False