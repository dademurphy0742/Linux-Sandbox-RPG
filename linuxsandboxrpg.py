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
# Utility
# -------------------------------
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# -------------------------------
# Load Commands
# -------------------------------
def load_commands(filename):
    with open(filename, "r") as f:
        data = json.load(f)
    return data["commands"]

# -------------------------------
# Dataset Selection
# -------------------------------
def choose_dataset():
    clear_screen()
    print("🔥 Linux Sandbox RPG 🔥\n")
    print("Select Mode:")
    print("1) Linux Basics")
    print("2) Kali / Pentesting")

    choice = input("\nEnter choice (1 or 2): ").strip()

    if choice == "1":
        return "datasets/linux_commands.json"
    elif choice == "2":
        return "datasets/kali_commands.json"
    else:
        print("Invalid choice, defaulting to Linux Basics.")
        return "datasets/linux_commands.json"

# -------------------------------
# Multiple Choice Generator
# -------------------------------
def generate_choices(correct_cmd):
    choices = [correct_cmd]

    # Get random incorrect commands
    while len(choices) < 4:
        cmd = random.choice(commands)["cmd"]
        if cmd not in choices:
            choices.append(cmd)

    random.shuffle(choices)
    return choices

# -------------------------------
# Game Logic
# -------------------------------
def game_intro():
    clear_screen()
    print("🔥 Linux Sandbox RPG (Multiple Choice Edition) 🔥\n")
    print("Learn Linux and pentesting commands interactively.\n")
    print("Choose the correct command based on the hint.\n")
    input("Press Enter to begin...")

def play_round():
    global score, level, streak

    command = random.choice(commands)
    correct = command["cmd"]

    choices = generate_choices(correct)
    labels = ["A", "B", "C", "D"]

    clear_screen()
    print(f"Level {level} | Score: {score} | Streak: {streak}")
    print(f"\n💡 Hint: {command['desc']}\n")

    # Display choices
    for i, choice in enumerate(choices):
        print(f"{labels[i]}) {choice}")

    answer = input("\nYour answer (A/B/C/D): ").strip().upper()

    if answer in labels:
        selected = choices[labels.index(answer)]

        if selected == correct:
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
            print(f"Correct answer: {correct}")

    else:
        print("\n⚠️ Invalid input. Please enter A, B, C, or D.")
        return

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
    global commands
    dataset_file = choose_dataset()
    commands = load_commands(dataset_file)
    game_intro()

    while True:
        play_round()
        cont = input("\nContinue playing? (y/n): ").strip().lower()
        if cont != 'y':
            print(f"\n🏆 Final Score: {score} | Level: {level}")
            print("Good luck mastering Linux and Kali tools 🚀")
            break

if __name__ == "__main__":
    main()
