Here’s an updated README based on your current one, with clarified install steps, corrected Python dependencies, and notes about Ollama CLI usage and model downloading — no venv, no unnecessary steps, and instructions that actually match the current Ollama usage:

---

# AI-Terminal

Natural Language to Linux Commands Terminal Interface

Welcome to **AI Terminal** — a smart terminal interface that lets you type commands in natural English and get real Linux shell commands suggested and executed by a local AI model. Great for beginners, automation lovers, or anyone who wants to avoid memorizing shell syntax.

---

## 🧠 What It Does

* You type something like: `delete all mp3 files in Downloads`
* AI suggests: `rm ~/Downloads/*.mp3`
* AI explains: `# Deletes all .mp3 files in the Downloads folder.`
* You confirm by pressing `Enter` to run, or skip with `Space` or `n`

---

## 📦 Requirements

* Linux, macOS, or WSL
* Python 3.7 or higher (no virtual environment required)
* [Ollama](https://ollama.com) desktop app installed (includes the CLI)
* Local Ollama AI model (e.g., `mistral`)

---

## 🛠️ Setup Instructions

### 1. Install Python dependencies

```bash
pip install requests
```

*(Only `requests` is required for the script to call Ollama’s API.)*

---

### 2. Install Ollama

Download and install Ollama manually from [https://ollama.com/download](https://ollama.com/download)

*Currently, there is no official CLI installer for Ollama itself.*
You can download the installer for your OS and install Ollama like any normal desktop app.

---

### 3. Download the AI model (e.g., mistral)

Once Ollama is installed, open your terminal and run:

```bash
ollama pull mistral
```

This downloads the `mistral` AI model locally.

---

### 4. Run the AI Terminal

Start the Python script:

```bash
python ai_terminal.py
```

---

## 🧪 Usage Example

```bash
> make a folder called test

AI Suggestion:
mkdir test
# Creates a directory named 'test'.

Run this command? (Enter = yes, space or 'n' = no):
```

---

## 💡 Notes

* The default AI model is `mistral` but you can specify others supported by Ollama.
* All AI processing happens locally — no cloud calls or data sharing.
* The AI Terminal **never runs commands without your explicit confirmation.**
* You don’t need to run `ollama serve` separately; the `ollama` CLI handles the model calls.

---

## 🚀 Tips

* Use this tool to learn shell commands in a safe, interactive way.
* Modify the system prompt in `ai_terminal.py` to customize AI behavior or add safety checks.

---

## 🧼 Uninstall Ollama

To remove the model and Ollama data:

```bash
ollama rm mistral
rm -rf ~/.ollama
```

Uninstall the Ollama app via your OS normal method (e.g., drag to trash on macOS).

---

Created with ❤️ by Hitarth

---

Let me know if you want me to add any OS-specific tips or automated installation scripts!
