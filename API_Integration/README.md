# Multi-Provider AI Chat Integrations

A collection of Python scripts that demonstrate how to integrate with **six different AI provider APIs**. Each provider has its own standalone file, plus a unified `multiapi.py` that lets you switch between all of them in one place.

---

## 📁 Repository Structure

```
.
├── openai_chat.py        # OpenAI GPT-4o
├── groq_chat.py          # Groq — LLaMA-3 70B
├── ollama_chat.py        # Ollama (local, no API key)
├── huggingface_chat.py   # Hugging Face Inference API
├── gemini_chat.py        # Google Gemini 1.5 Flash
├── cohere_chat.py        # Cohere Command R+
├── multiapi.py           # All-in-one interactive selector
├── requirements.txt      # Python dependencies
└── README.md             # This file
```

---

## ⚙️ Setup

### 1. Clone the Repository
```bash
git clone https://github.com/<your-username>/multi-ai-apis.git
cd multi-ai-apis
```

### 2. Create a Virtual Environment (Recommended)
```bash
python -m venv venv
source venv/bin/activate        # Linux / macOS
venv\Scripts\activate           # Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Environment Variables

**Never hardcode API keys.** Export them in your shell before running:

```bash
# OpenAI
export OPENAI_API_KEY="sk-..."

# Groq
export GROQ_API_KEY="gsk_..."

# Hugging Face
export HF_API_KEY="hf_..."

# Google Gemini
export GEMINI_API_KEY="AIza..."

# Cohere
export COHERE_API_KEY="..."

# Ollama (optional overrides)
export OLLAMA_HOST="http://localhost:11434"   # default
export OLLAMA_MODEL="llama3"                 # default
```

> On Windows use `set KEY=value` or configure via System Environment Variables.

---

## 🚀 Running the Scripts

### Individual Providers

```bash
python openai_chat.py
python groq_chat.py
python ollama_chat.py
python huggingface_chat.py
python gemini_chat.py
python cohere_chat.py
```

### All-in-One Interface

```bash
# Interactive provider selection menu
python multiapi.py

# Start directly with a specific provider
python multiapi.py --provider openai
python multiapi.py --provider groq
python multiapi.py --provider ollama
python multiapi.py --provider hf
python multiapi.py --provider gemini
python multiapi.py --provider cohere
```

Type `back` to return to the provider menu, `exit` to quit.

---

## 🤖 Providers & Models

| Script               | Provider       | Model                            | Key Env Var         |
|----------------------|----------------|----------------------------------|---------------------|
| `openai_chat.py`     | OpenAI         | gpt-4o                           | `OPENAI_API_KEY`    |
| `groq_chat.py`       | Groq           | llama3-70b-8192                  | `GROQ_API_KEY`      |
| `ollama_chat.py`     | Ollama (local) | llama3 (configurable)            | none                |
| `huggingface_chat.py`| Hugging Face   | Mistral-7B-Instruct-v0.2         | `HF_API_KEY`        |
| `gemini_chat.py`     | Google Gemini  | gemini-1.5-flash                 | `GEMINI_API_KEY`    |
| `cohere_chat.py`     | Cohere         | command-r-plus                   | `COHERE_API_KEY`    |

---

## 🔑 Obtaining API Keys

| Provider       | URL                                               |
|----------------|---------------------------------------------------|
| OpenAI         | https://platform.openai.com/api-keys             |
| Groq           | https://console.groq.com/keys                    |
| Ollama         | https://ollama.com (local, no key needed)         |
| Hugging Face   | https://huggingface.co/settings/tokens           |
| Google Gemini  | https://aistudio.google.com/app/apikey            |
| Cohere         | https://dashboard.cohere.com/api-keys            |

---

## 🛡️ Error Handling

Every script handles:
- **Missing API key** — clear message telling which env var to set
- **Missing package** — install command shown
- **Network / HTTP errors** — error code and message displayed
- **Unexpected exceptions** — caught and printed without crashing

---

## 📸 Screenshots

Screenshots of each program running are located in the `/screenshots` folder.

---

## 📄 License

MIT License — feel free to use, modify, and distribute.
