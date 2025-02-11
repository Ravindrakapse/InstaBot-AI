# InstaBot-AI

## 🚀 Automatic AI-Powered Instagram Content Creator

InstaBot-AI is a fully automated Instagram content creation and posting bot. It generates creative prompts, captions, and high-quality images using AI models and posts them on Instagram (@bebrave486) every hour, requiring zero human intervention.

## ✨ Features
- **AI-Powered Prompt & Caption Generation**: Uses `deepseek-R1` to generate engaging prompts and captions.
- **Image Creation with FLUX**: Generates stunning AI art using the `FLUX.1-dev` model.
- **Automated Instagram Posting**: Uses `instagrapi` to post AI-generated content to Instagram.
- **Completely Hands-Free**: Runs automatically without human input.

---

## 📂 Project Structure
```
📦 InstaBot-AI
├── 📂 out/                 # Output folder for generated images
├── 📄 .gitignore           # Git ignore file
├── 📄 .python-version      # Python version specification (3.12)
├── 📄 README.md            # Project documentation
├── 📄 hello.py             # Redundant file
├── 📄 main.py              # Main execution script
├── 📄 plus.py              # Core functions for AI generation & posting
├── 📄 pyproject.toml       # Python dependencies & metadata
├── 📄 uv.lock              # Package lock file
```

---

## 🛠️ Installation & Setup
### Prerequisites
- Python **3.12**
- `deepseek-R1` (7B model)
- `FLUX.1-dev`
- Instagram account login session (`session.json`)

### Running the Bot
To start the bot, simply run:
```bash
python main.py
```
This will:
1. Generate an **image prompt** and **caption**.
2. Use `FLUX.1-dev` to create an image.
3. Automatically post the image with the caption to Instagram.

---

## ⚙️ How It Works
### 1️⃣ Generating Image Prompts & Captions
- Uses `deepseek-R1` to generate creative prompts and captions.
- Extracts structured data from AI response using regex.

### 2️⃣ AI Image Creation
- Uses `FLUX.1-dev` to generate high-resolution images based on the prompt.
- Ensures consistent quality and creativity.

### 3️⃣ Automated Instagram Posting
- Uploads the AI-generated image to Instagram using `instagrapi`.
- Posts at regular intervals without manual intervention.

---

## 📌 Example Output
**Prompt:**  *"Walter White (Heisenberg) from Breaking bad webseries teaching chemistry in a high school classroom wearing an overalls and a lab coat with strange symbols, using a pipe as a beaker."*

**Caption:**  *Chemistry 101 with a pipe" - the students look confused. #ChemistryFun #ScienceHumor*

**Image:**  
![Generated Image](out/Creative_bb_0.png)

---

## 🛠️ Dependencies
```toml
[tool.poetry]
name = "instabot-ai"
version = "0.1.0"
description = "Fully automated AI-powered Instagram bot"
readme = "README.md"
requires-python = ">=3.12"

[tool.poetry.dependencies]
diffusers = ">=0.32.2"
instagrapi = ">=2.1.3"
numpy = ">=2.2.2"
ollama = ">=0.4.7"
torch = ">=2.6.0"
```

---

## 🏆 Future Improvements
- Integrate **GPT-4** for better prompt engineering.
- Allow users to customize **content themes**.
- Implement **multi-account posting**.

🚀 Enjoy fully automated AI-powered Instagram content creation! 🚀

