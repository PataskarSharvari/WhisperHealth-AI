# 🏥 WhisperHealth - Your AI Medical Assistant 🤖🩺
**WhisperHealth** is an AI-powered multimodal medical assistant chatbot, combining **Vision**, **Voice**, and **Natural Language Understanding**. Designed with real-time voice interaction, image analysis, and context-aware medical responses, this AI bot aims to assist users with medical-related queries through a conversational interface. Here I have built a multimodal AI chatbot using LLaMA3 Vision, OpenAI Whisper, and Groq LLMs for real-time medical Q&A.

Integrated speech-to-text, image analysis, and LLM inference to generate voice-based medical guidance.

Designed a voice-enabled UI with Gradio; deployed live on Hugging Face Spaces.

Technologies: Python, Whisper, Gradio, Groq API, gTTS, ffmpeg, .env, Hugging Face.

🌐 **[Live Demo on Hugging Face Spaces](https://huggingface.co/spaces/Sharvari19/WhisperHealth-AI-Medical-Chatbot)**

---

## 🧠 Features

- 🎙️ Voice-based patient interaction using speech recognition.
- 👁️ Vision capabilities using LLaMA 3 Vision for image-based queries.
- 💬 Conversational AI using GROQ API for fast, accurate LLM inference.
- 🗣️ Text-to-Speech response via gTTS.
- 🌐 Clean and intuitive Gradio UI for seamless interaction.

---

## 🛠️ Tech Stack

| Layer            | Tool / Library         |
|------------------|------------------------|
| LLM Inference    | GROQ API               |
| Vision Model     | LLaMA 3 Vision         |
| Transcription    | OpenAI Whisper         |
| Text to Speech   | gTTS (or ElevenLabs )  |
| UI Layer         | Gradio                 |
| Language         | Python                 |
| Dev Environment  | VS Code                |

---

## 🗂️ Project Structure

```bash
📁 ai-medical-chatbot/
│
├── brain_of_the_doctor.py         # Multimodal model handling (Vision + LLM)
├── voice_of_the_patient.py        # Handles recording and transcription
├── voice_of_the_doctor.py         # Text-to-speech generation
├── app.py                         # Main Gradio app interface
├── assets/                        # UI assets and sample images
├── requirements.txt               # Python dependencies
├── README.md                      # Project overview and guide
└── .env                           # Your API keys (not pushed to GitHub)
```

---

## 🔁 Project Flow

```
Voice Input → Whisper Transcription (STT)
                ↓
       User Query (Text or Image)
                ↓
         GROQ + LLaMA 3 Vision
                ↓
         Text Response Generated
                ↓
        TTS via gTTS / ElevenLabs
                ↓
            Voice Output
                ↓
            Display in Gradio
```

---

## ⚙️ Installation & Setup

> Tested on Python 3.9+

### 🔐 1. Clone the Repository

```bash
git clone https://github.com/PataskarSharvari/ai-medical-chatbot.git
cd ai-medical-chatbot
```

### 📦 2. Create a Virtual Environment (optional but recommended)

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
```

### 📦 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 🔑 4. Add Your API Keys

Create a `.env` file and add the following:

```env
GROQ_API_KEY=your_groq_api_key
```

### 🔊 5. Install Required Audio Libraries

Install `ffmpeg` and `portaudio`:

- **Windows**: Use [FFmpeg builds](https://www.gyan.dev/ffmpeg/builds/) and install `portaudio` using `pip install pyaudio`.
- **Linux**: Use `sudo apt install ffmpeg portaudio19-dev`

---

## 🚀 How to Run Locally

```bash
python app.py
```

> A Gradio interface will launch in your browser at `http://localhost:7860`.

---

> For live demo, visit [WhisperHealth on Hugging Face](https://huggingface.co/spaces/SharvariPataskar/WhisperHealth-AI)

---

## 🧩 Dependencies

```txt
gradio
openai-whisper
pyaudio
ffmpeg
groq
gtts
elevenlabs
python-dotenv
```

---

## 📈 Roadmap & Future Improvements

- 💰 Upgrade to state-of-the-art paid Vision LLMs (e.g. Gemini, Claude)
- 🧠 Finetune LLaMA-3 Vision model on medical datasets
- 🌐 Add multilingual support (Hindi, Marathi, etc.)
- 🧾 Store past interactions securely with MongoDB and add RAG (Retrieval-Augmented Generation) with medical knowledge base.
- 📱 Mobile optimized frontend (React Native)

---

## 🤝 Contributing

Pull requests and feature suggestions are welcome. Please open an issue first to discuss what you would like to change.

---

## 📜 License

MIT License

---

## 📬 Contact

- 👩‍💻 Developer: [Sharvari Pataskar](https://github.com/PataskarSharvari)
  
---

## ✨ Acknowledgements

- [Meta LLaMA 3 Vision](https://llama.meta.com/)
- [Groq API](https://console.groq.com/)
- [Gradio](https://www.gradio.app/)
- [OpenAI Whisper](https://github.com/openai/whisper)

