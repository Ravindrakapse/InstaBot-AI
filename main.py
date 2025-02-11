import numpy as np
import random 
import os
from plus import *


# Lists of variables
characters = ["Walter White", "Jesse Pinkman", "Skyler White"]
activities = ["making pancakes", "teaching chemistry to kids", "running a lemonade stand"]
settings = ["a retro diner", "a high school classroom", "a suburban backyard"]


def main():
    try:
        image_prompt, image_caption = generate_prompt_caption(characters,activities,settings)

        # Generate image if prompt was extracted successfully
        if image_prompt and image_caption:
            print("\nGenerating image and posting to Instagram...")
            generate_image(image_prompt, image_caption)
        else:
            print("\nSkipping image generation due to missing prompt or caption")

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        # print("Full response for debugging:")
        # print(content)

if __name__ == "__main__":
    main()
