# ai_terminal.py

import subprocess
import readline
import requests
import json
import re

MODEL_NAME = 'mistral'
OLLAMA_API_URL = 'http://localhost:11434/api/chat'

INTRO = '''\nWelcome to AI-Terminal!
Type commands in natural English (e.g., "list all files in this folder").
Press Enter to run the AI-suggested command. Press Space or type 'skip' to skip it.\n'''

PROMPT = '> '

def extract_command(response_text):
    """
    Extract the first shell command from the AI response.
    Supports extracting code blocks and inline commands.
    """
    # Try to find a bash or shell code block first
    code_block_match = re.search(r'```(?:bash|sh)?\n(.*?)```', response_text, re.DOTALL)
    if code_block_match:
        command = code_block_match.group(1).strip()
        # Sometimes code blocks have multiple lines; take the first line as command
        return command.splitlines()[0]

    # If no code block, fallback to first line that looks like a command (not starting with # or explanation)
    for line in response_text.splitlines():
        line = line.strip()
        if line and not line.startswith('#') and not line.lower().startswith('to find') and not line.startswith('```'):
            return line

    # If all else fails, return the first line anyway
    return response_text.splitlines()[0].strip()

def get_command_from_ai(prompt):
    system_message = (
        "You are an expert Linux assistant. Given a natural language instruction, return only one shell command, and then one short explanation.\n"
        "Example:\nInput: delete all mp3 files from downloads\nOutput:\nrm ~/Downloads/*.mp3\n# Deletes all .mp3 files in the Downloads folder."
    )

    url = OLLAMA_API_URL
    payload = {
        "model": MODEL_NAME,
        "messages": [
            {"role": "system", "content": system_message},
            {"role": "user", "content": prompt}
        ],
        "stream": True
    }

    try:
        response = requests.post(url, json=payload, stream=True)
        response.raise_for_status()

        full_response = ""
        for line in response.iter_lines():
            if line:
                data = line.decode('utf-8')
                json_data = json.loads(data)
                if 'message' in json_data and 'content' in json_data['message']:
                    full_response += json_data['message']['content']

        return full_response.strip()

    except Exception as e:
        print(f"\n[!] Error contacting Ollama API: {e}\n")
        return "# Failed to get response from AI."

def run_shell_command(cmd):
    try:
        subprocess.run(cmd, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"\n[!] Command failed: {e}\n")

print(INTRO)

while True:
    try:
        user_input = input(PROMPT).strip()
        if not user_input:
            continue
        if user_input.lower() in ('exit', 'quit'):
            break

        result = get_command_from_ai(user_input)

        # Extract command cleanly from AI response
        command = extract_command(result)
        explanation = result.replace(command, '').strip()

        print(f"\nAI Suggestion:\n{command}\n{explanation}\n")
        proceed = input("Run this command? (Enter = yes, space or 'n' = no): ").strip().lower()

        if proceed in ('', 'y', 'yes'):
            run_shell_command(command)
        else:
            print("[i] Command skipped.\n")

    except KeyboardInterrupt:
        print("\n[i] Exiting...")
        break
    except Exception as e:
        print(f"[!] Error: {e}")
