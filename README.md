# Implementation-of-ProxyLLM
Implementation of ProxyLLM using LM Studio

## ProxyLLM — Local LLM-Powered Customer Support Text Styler

A lightweight, developer-friendly framework that rewrites customer support messages into neutral, polite, or professional tones using locally hosted Large Language Models (LLMs) via LM Studio and Python.

Inspired by the [ProxyLLM](https://github.com/sehyeongjo/Proxy-LLM) research paper, this implementation offers a practical way to integrate AI-driven text rewording directly into customer support workflows without sending sensitive data to external APIs.

---

## 💡 Features

- 🧠 **Tone Transfer:** Rewrite negative or emotional customer messages into a friendly or neutral tone.
- ⚡️ **Local Inference:** Run fully offline via LM Studio.
- 🔍 **Sentiment Analysis:** Detects sentiment using NLTK before sending to the LLM.
- 🔌 **Easy Integration:** Pair with a Chrome Extension or web apps.

---

## 🏗️ Architecture Overview

User Input ➡️ Python Backend ➡️ Sentiment Analysis ⬇️ If Negative ➡️ LM Studio Local LLM ➡️ Rewritten Text ⬇️ Client or Chrome Extension


---

## 🚀 Setup Instructions

### 1️⃣ Prerequisites

- Python 3.8+
- LM Studio (Download: https://lmstudio.ai/)
- An LLM model loaded in LM Studio (`Llama3-Instruct` or `Mistral-Instruct` recommended).

---

### 2️⃣ Install Dependencies

```bash
pip install flask requests nltk
```

And download the NLTK sentiment model:

```bash
import nltk
nltk.download('vader_lexicon')
```

### 3️⃣ LM Studio Setup

Open LM Studio.
Load your preferred gguf model (example: llama-3-8b-instruct.Q4_K_M.gguf).

Go to API Server tab and:
✅ Enable Allow requests from any origin.
Note the server address: http://localhost:1234.


### 4️⃣ Run the Python Server
Save the following as app.py:
(See full code in the app.py file.)

Start your server:

```
python app.py
```

### 5️⃣ Test the Endpoint
Using curl:

```
curl -X POST http://localhost:5000/transform \
  -H "Content-Type: application/json" \
  -d '{"text":"Your service is absolutely terrible!"}'
```
Expected Response:

```
{"transformed":"I am very disappointed with the service I received. Could you please assist me with this issue?"}
```

💡 Chrome Extension Integration

You can pair this server with a Chrome Extension to automatically rewrite customer support chat text before sending. See extension/ for an example.

## ⚠️ Common Errors & Troubleshooting


### Issue	Cause	Fix
ConnectionError: Failed to establish a new connection	LM Studio not running or API Server not enabled.	Launch LM Studio and check API Server settings.
{"error":"model not loaded"}	Model not selected in LM Studio.	Select a model in LM Studio GUI.
KeyError: 'choices'	LM Studio response format unexpected.	Log response.text to debug the issue.
LookupError: vader_lexicon not found.	NLTK sentiment model missing.	Run nltk.download('vader_lexicon').
Requests time out or hang.	LM Studio slow or large input size.	Add timeout=60 in your requests.post().

### 🧠 Best Practices

Use chat-tuned models (instruct) for best results.
Test sentiment detection on sample text before production use.
Add fallback responses in case LM Studio is unavailable.

### 🏁 Roadmap

 Multi-tone output (friendly, apologetic, professional).
 Docker deployment.
 Chrome Extension auto-install package.
 Logging & retry logic for production.

### 💬 Credits

This project is inspired by ProxyLLM and designed for real-world, locally-hosted LLM customer support systems.

### 📄 License

MIT — feel free to use, modify, and extend!
