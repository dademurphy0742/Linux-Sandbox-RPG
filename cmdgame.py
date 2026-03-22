#!/usr/bin/env python3
import os
import random
import shutil
import subprocess
import tempfile
import time

# -------------------------------
# Game variables
# -------------------------------
score = 0
level = 1
streak = 0

# -------------------------------
# Allowed Linux commands in sandbox
# -------------------------------
allowed_commands = [
    "ls", "pwd", "cd", "mkdir", "rmdir", "touch", "rm", "cp", "mv", "tree",
    "cat", "head", "tail", "less", "nano", "vim", "grep", "wc", "echo",
    "uname", "whoami", "id", "date", "uptime", "ps", "top", "free", "df",
    "du", "ping", "curl", "wget", "tar", "gzip", "gunzip", "zip", "unzip",
    "alias", "history", "sleep", "chmod", "chown", "env", "export", "source",
    "clear", "dmesg"
]

# -------------------------------
# Hints for learning
# -------------------------------
command_hints = {
    "ls": "List files and directories",
    "pwd": "Show current directory",
    "cd": "Change directory",
    "mkdir": "Create a new directory",
    "rmdir": "Remove empty directories",
    "touch": "Create a new file",
    "rm": "Remove files or directories",
    "cp": "Copy files or directories",
    "mv": "Move or rename files",
    "tree": "Show directory tree",
    "cat": "Show file contents",
    "head": "Show first lines of a file",
    "tail": "Show last lines of a file",
    "less": "View file content interactively",
    "nano": "Open a text editor",
    "vim": "Open a powerful text editor",
    "grep": "Search for text inside files",
    "wc": "Count lines, words, characters",
    "echo": "Print text",
    "uname": "Show system info",
    "whoami": "Show current user",
    "id": "Show user and group IDs",
    "date": "Show current date/time",
    "uptime": "Show system uptime and load",
    "ps": "List processes",
    "top": "Monitor running processes",
    "free": "Show memory usage",
    "df": "Show disk usage",
    "du": "Show folder/file size",
    "ping": "Check network connectivity",
    "curl": "Download data from a server",
    "wget": "Download files",
    "tar": "Archive files",
    "gzip": "Compress files",
    "gunzip": "Decompress files",
    "zip": "Compress files into zip",
    "unzip": "Extract zip files",
    "alias": "Create command shortcut",
    "history": "Show command history",
    "sleep": "Pause execution",
    "chmod": "Change file permissions",
    "chown": "Change file owner",
    "env": "Show environment variables",
    "export": "Set environment variables",
    "source": "Execute commands from file",
    "clear": "Clear the screen",
    "dmesg": "Show kernel logs",
}

# -------------------------------
# Utility functions
# -------------------------------
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def run_command(command, sandbox_path):
    """Run a command safely inside sandbox."""
    parts = command.strip().split()
    if not parts:
        return
    
    cmd = parts[0]
    if cmd not in allowed_commands:
        print(f"⚠️ Command '{cmd}' is not allowed in the sandbox.")
        return
    
    try:
        # Run the command safely inside sandbox
        result = subprocess.run(parts, cwd=sandbox_path, capture_output=True, text=True, shell=False)
        if result.stdout:
            print(result.stdout)
        if result.stderr:
            print(result.stderr)
    except Exception as e:
        print(f"Error: {e}")

# -------------------------------
# Game logic
# -------------------------------
def game_intro():
    clear_screen()
    print("🔥 Welcome to Linux Sandbox RPG! 🔥\n")
    print("Explore, create, and manipulate files in your safe virtual Linux environment.")
    print("Earn points for using commands correctly and completing missions.\n")
    input("Press Enter to enter your sandbox...")

def play_round(sandbox_path):
    global score, level, streak
    
    # Pick a random command hint for the player
    cmd, hint = random.choice(list(command_hints.items()))
    
    clear_screen()
    print(f"Level {level} | Score: {score} | Streak: {streak}")
    print(f"\n💡 Hint: {hint}")
    print(f"📂 Sandbox Path: {sandbox_path}\n")
    
    answer = input("Type the Linux command here: ").strip()
    
    if answer.startswith(cmd):
        points = random.randint(5, 15)
        score += points
        streak += 1
        print(f"✅ Correct usage! You earned {points} points.")
        if streak > 2:
            bonus = streak * 2
            score += bonus
            print(f"🔥 Streak bonus! +{bonus} points.")
        run_command(answer, sandbox_path)
    else:
        points = random.randint(3, 10)
        score -= points
        streak = 0
        print(f"❌ Wrong or incomplete command. The correct command starts with '{cmd}'. You lost {points} points.")
    
    # Level up every 50 points
    if score >= level * 50:
        level += 1
        print(f"\n🎉 Congratulations! You've reached Level {level}!")
    
    time.sleep(2)

# -------------------------------
# Main function
# -------------------------------
def main():
    game_intro()
    
    # Create sandbox directory
    sandbox_path = tempfile.mkdtemp(prefix="linux_sandbox_")
    
    try:
        while True:
            play_round(sandbox_path)
            cont = input("\nContinue playing? (y/n): ").strip().lower()
            if cont != 'y':
                print(f"\n🏆 Final Score: {score} | Reached Level: {level}")
                break
    finally:
        # Clean up sandbox
        shutil.rmtree(sandbox_path)
        print("\nSandbox deleted. All changes were temporary. Thanks for playing! 🚀")

if __name__ == "__main__":
    main()
