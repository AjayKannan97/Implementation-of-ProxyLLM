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
