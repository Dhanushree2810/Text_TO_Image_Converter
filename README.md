# 🎨 DreamForge — Text-to-Image Generator

DreamForge is a lightweight AI-based text-to-image generator built using Python and Hugging Face InferenceClient. It converts user prompts into high-quality images with style options and built-in safety filtering, all through a simple local web interface.

---

## 🚀 Features

* 🖼️ Generate images from text prompts
* 🎨 Multiple styles (Anime, Cinematic, Digital Art, etc.)
* 🔄 Automatic fallback across multiple AI models
* 🔒 NSFW content filtering
* 💻 Clean and simple UI
* ⚡ Runs locally

---

## 🛠️ Tech Stack

* Python
* Hugging Face API
* HTML, CSS, JavaScript
* HTTP Server

---

## 📂 Project Structure

TEXT_TO_IMAGE_CONVERTER/
│
├── app.py                 # Main server + UI (HTML inside)
│
├── core/
│   ├── api.py             # Image generation logic
│   └── safety.py          # NSFW filter
│
├── requirements.txt       # (optional) dependencies
└── README.md              # Project documentation

---

## ⚙️ Installation

1. Clone the repository:
   git clone https://github.com/your-username/dreamforge.git
   cd dreamforge

2. Install dependencies:
   pip install huggingface_hub requests

---

## 🔑 API Token

1. Go to https://huggingface.co
2. Settings → Access Tokens
3. Create a new token (Write)
4. Copy token (starts with hf_)

---

## ▶️ Run the Project

python app.py

Open in browser:
http://localhost:8080

---

## 🧠 How It Works

* User enters a prompt
* Request is sent to Hugging Face models
* Multiple models are tried automatically
* Image is generated and displayed
* User can download the image

---

## ⚠️ Notes

* Internet connection required
* API limits may apply
* Generation takes ~20–60 seconds

---

## 📌 Author

Dhanushree Arangaswamy

---


