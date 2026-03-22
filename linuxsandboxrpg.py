#!/usr/bin/env python3
import random
import os

# -------------------------------
# Game State
# -------------------------------
score = 0
level = 1
streak = 0

# -------------------------------
# Command Database (expandable)
# -------------------------------
commands = [
    {
        "cmd": "ls",
        "desc": "List files and directories",
        "explanation": "Displays files and directories in the current location.",
        "usage": "ls [options] [directory]",
        "examples": [
            "ls",
            "ls -la",
            "ls /home/user"
        ]
    },
    {
        "cmd": "pwd",
        "desc": "Print current working directory",
        "explanation": "Shows the full path of your current directory.",
        "usage": "pwd",
        "examples": [
            "pwd"
        ]
    },
    {
        "cmd": "cd",
        "desc": "Change directory",
        "explanation": "Moves you into another directory.",
        "usage": "cd [directory]",
        "examples": [
            "cd /home/user",
            "cd ..",
            "cd ~"
        ]
    },
    {
        "cmd": "mkdir",
        "desc": "Create a new directory",
        "explanation": "Creates one or more directories.",
        "usage": "mkdir [directory_name]",
        "examples": [
            "mkdir test",
            "mkdir folder1 folder2",
            "mkdir -p parent/child"
        ]
    },
    {
        "cmd": "touch",
        "desc": "Create a new empty file",
        "explanation": "Creates a new file or updates a file timestamp.",
        "usage": "touch [file]",
        "examples": [
            "touch file.txt",
            "touch file1 file2"
        ]
    },
    {
        "cmd": "cp",
        "desc": "Copy files or directories",
        "explanation": "Copies files or directories from one location to another.",
        "usage": "cp [source] [destination]",
        "examples": [
            "cp file.txt backup.txt",
            "cp -r folder1 folder2",
            "cp file.txt /home/user/Documents/"
        ]
    },
    {
        "cmd": "mv",
        "desc": "Move or rename files",
        "explanation": "Moves or renames files and directories.",
        "usage": "mv [source] [destination]",
        "examples": [
            "mv file.txt newname.txt",
            "mv file.txt /home/user/"
        ]
    },
    {
        "cmd": "rm",
        "desc": "Remove files or directories",
        "explanation": "Deletes files or directories permanently.",
        "usage": "rm [options] [file]",
        "examples": [
            "rm file.txt",
            "rm -r folder",
            "rm -f file.txt"
        ]
    },
    {
        "cmd": "cat",
        "desc": "Display file contents",
        "explanation": "Prints file contents to the terminal.",
        "usage": "cat [file]",
        "examples": [
            "cat file.txt",
            "cat file1 file2"
        ]
    },
    {
        "cmd": "grep",
        "desc": "Search for text in files",
        "explanation": "Searches for patterns inside files.",
        "usage": "grep [pattern] [file]",
        "examples": [
            "grep 'error' log.txt",
            "grep -r 'hello' .",
            "grep -i 'word' file.txt"
        ]
    },
    {
        "cmd": "chmod",
        "desc": "Change file permissions",
        "explanation": "Modifies file access permissions.",
        "usage": "chmod [permissions] [file]",
        "examples": [
            "chmod +x script.sh",
            "chmod 755 file.txt"
        ]
    },
    {
        "cmd": "chown",
        "desc": "Change file ownership",
        "explanation": "Changes the owner and group of a file.",
        "usage": "chown [user]:[group] [file]",
        "examples": [
            "chown user file.txt",
            "chown user:group file.txt"
        ]
    },
    {
        "cmd": "df",
        "desc": "Show disk space usage",
        "explanation": "Displays available and used disk space.",
        "usage": "df [options]",
        "examples": [
            "df",
            "df -h"
        ]
    },
    {
        "cmd": "du",
        "desc": "Show file/directory size",
        "explanation": "Estimates file space usage.",
        "usage": "du [options] [file]",
        "examples": [
            "du -sh *",
            "du -h folder"
        ]
    },
    {
        "cmd": "ps",
        "desc": "Show running processes",
        "explanation": "Displays currently running processes.",
        "usage": "ps [options]",
        "examples": [
            "ps",
            "ps aux"
        ]
    },
    {
        "cmd": "top",
        "desc": "Monitor system processes",
        "explanation": "Shows real-time system processes.",
        "usage": "top",
        "examples": [
            "top"
        ]
    },
    {
        "cmd": "echo",
        "desc": "Print text to terminal",
        "explanation": "Outputs text or variables.",
        "usage": "echo [text]",
        "examples": [
            "echo Hello",
            "echo $HOME"
        ]
    },
    {
        "cmd": "whoami",
        "desc": "Show current user",
        "explanation": "Displays the current logged-in user.",
        "usage": "whoami",
        "examples": [
            "whoami"
        ]
    },
    {
        "cmd": "uname",
        "desc": "Show system information",
        "explanation": "Displays system details.",
        "usage": "uname [options]",
        "examples": [
            "uname",
            "uname -a"
        ]
    }
]

# -------------------------------
# Utility
# -------------------------------
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# -------------------------------
# Game Logic
# -------------------------------
def game_intro():
    clear_screen()
    print("🔥 Linux Command RPG (Trivia Edition) 🔥\n")
    print("Learn Linux commands through gameplay.\n")
    print("Type the correct command based on the hint.\n")
    input("Press Enter to begin...")

def play_round():
    global score, level, streak
    
    command = random.choice(commands)
    
    clear_screen()
    print(f"Level {level} | Score: {score} | Streak: {streak}")
    print(f"\n💡 Hint: {command['desc']}\n")
    
    answer = input("Type the Linux command: ").strip()
    
    if answer == command["cmd"]:
        points = random.randint(5, 15)
        score += points
        streak += 1
        
        print(f"\n✅ Correct! +{points} points")
        
        if streak > 2:
            bonus = streak * 2
            score += bonus
            print(f"🔥 Streak bonus! +{bonus}")
    
    else:
        points = random.randint(3, 10)
        score -= points
        streak = 0
        
        print(f"\n❌ Incorrect. -{points} points")
        print(f"Correct answer: {command['cmd']}")
    
    # -------------------------------
    # Learning Section
    # -------------------------------
    print("\n📘 Explanation:")
    print(command["explanation"])
    
    print("\n⚙️ Usage:")
    print(command["usage"])
    
    print("\n💻 Examples:")
    for ex in command["examples"]:
        print(f"  - {ex}")
    
    # Level up
    if score >= level * 50:
        level += 1
        print(f"\n🎉 Level Up! You are now Level {level}")
    
    input("\nPress Enter to continue...")

# -------------------------------
# Main
# -------------------------------
def main():
    game_intro()
    
    while True:
        play_round()
        cont = input("\nContinue playing? (y/n): ").strip().lower()
        if cont != 'y':
            print(f"\n🏆 Final Score: {score} | Level: {level}")
            print("Good luck mastering Linux 🚀")
            break

if __name__ == "__main__":
    main()
