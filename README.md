# AI-Terminal
# AI Terminal - Natural Language to Linux Commands

Welcome to **AI Terminal** — a smart terminal interface that lets you type English and get real Linux commands suggested and executed. Great for new users, automation enthusiasts, or anyone who wants to skip memorizing shell syntax.

## 🧠 What it Does

* You type something like: `delete all mp3 files in Downloads`
* AI suggests: `rm ~/Downloads/*.mp3`
* It explains: `# Deletes all .mp3 files in the Downloads folder.`
* You press `Enter` to run it or skip it with `Space`/`n`

## 📦 Requirements

* Linux (or WSL/macOS)
* Python 3.7+
* [Ollama](https://ollama.com) (for local AI model)

## 🛠️ Setup Instructions

### 1. Install Python dependencies

```bash
pip install ollama
```

### 2. Install Ollama

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

### 3. Download and run a model

```bash
ollama run mistral
```

Leave this terminal open in the background — this will keep the LLM running.

### 4. Run the AI Terminal

```bash
python ai_terminal.py
```

## 🧪 Usage Example

```bash
> make a folder called test

AI Suggestion:
mkdir test
# Creates a directory named 'test'.

Run this command? (Enter = yes, space or 'n' = no):
```

## 💡 Notes

* It uses `mistral` by default but you can switch to other local models supported by Ollama.
* All prompts and answers stay on your machine. Nothing is sent to the cloud.
* The AI won’t auto-run anything — it always confirms with you.

## 🚀 Tips

* Use this to learn shell syntax while you work
* Customize the system prompt in `ai_terminal.py` if you want more safety, verbosity, or different output styles

## 🧼 Uninstall

To remove Ollama:

```bash
ollama rm mistral
sudo rm -rf ~/.ollama
```

---

Created with ❤️ by Hitarth.
