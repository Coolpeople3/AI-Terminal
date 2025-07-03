# ai_terminal.py

import subprocess
import ollama
import readline

MODEL_NAME = 'mistral'

INTRO = '''\nWelcome to AI-Terminal!
Type commands in natural English (e.g., "list all files in this folder").
Press Enter to run the AI-suggested command. Press Space or type 'skip' to skip it.\n'''

PROMPT = '> '

def get_command_from_ai(prompt):
    system_message = (
        "You are an expert Linux assistant. Given a natural language instruction, return only one shell command, and then one short explanation.\n"
        "Example:\nInput: delete all mp3 files from downloads\nOutput:\nrm ~/Downloads/*.mp3\n# Deletes all .mp3 files in the Downloads folder."
    )

    response = ollama.chat(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": prompt}
        ]
    )

    return response["message"]["content"].strip()

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

        # Separate command and explanation
        lines = result.splitlines()
        command = lines[0]
        explanation = '\n'.join(lines[1:]) if len(lines) > 1 else ''

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
