#!/usr/bin/env python3
import json
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
def load_commands():
    with open("commands.json", "r") as f:
        data = json.load(f)
    return data["commands"]

commands = load_commands()

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
