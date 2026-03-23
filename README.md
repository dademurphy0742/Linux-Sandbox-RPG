<img width="1536" height="1024" alt="file_000000004cac71fd8c72c6b89a4d66a9" src="ChatGPT Image Mar 23, 2026, 09_05_42 AM.png" />

# 🔥 Linux Sandbox RPG (Multiple Choice Edition)

Learn Linux and Kali Linux commands through an interactive command-line game designed for **fast, effective skill building**.

---

## 🎮 Overview

Linux Sandbox RPG is a Python-based CLI game that helps you master Linux and penetration testing commands using a **multiple-choice gameplay system**.

Instead of memorizing commands passively, you:

* Analyze hints
* Choose the correct command
* Learn through instant feedback, explanations, and examples

---

## 🚀 Features

* ✅ **Multiple Choice Gameplay** — Choose from 4 possible answers
* 🧠 **Reinforced Learning Loop** — Hint → Answer → Explanation → Examples
* 📈 **Progression System** — Score, streaks, and leveling
* 🔥 **Streak Bonuses** — Reward consistency and accuracy
* 📚 **Data-Driven Design** — Easily expand commands via JSON
* 🛡️ **Safe Learning Environment** — No real system commands executed

---

## 🧩 Game Modes

You can plug in different datasets:

### 🐧 Linux Mode

* Core filesystem, shell, and system commands
* Beginner → Intermediate friendly

### 🛠️ Kali / Pentesting Mode

* Reconnaissance tools (`nmap`, `amass`)
* Exploitation tools (`sqlmap`, `msfconsole`)
* Password attacks (`hydra`, `hashcat`)
* Web, network, and post-exploitation tools

---

## ⚙️ Installation

1. Clone the repository:

```bash
git clone https://github.com/dademurphy0742/Linux-Sandbox-RPG/.git
cd Linux-Sandbox-RPG
```

2. Run the game:

```bash
python3 linuxsandboxrpg.py
```

---

## 🧠 How It Works

1. You are given a **hint** describing a command
2. You choose from **4 possible answers (A–D)**
3. The game evaluates your answer
4. You receive:

   * ✔ Correct/Incorrect feedback
   * 📘 Explanation
   * ⚙️ Usage syntax
   * 💻 Real examples

---

## 📊 Scoring System

* ✔ Correct answer → **+5 to +15 points**
* 🔥 Streak bonus → increases with consecutive correct answers
* ❌ Wrong answer → **-3 to -10 points**
* 🎉 Level up every **(level × 50) points**

---

## 🔧 Customization

Easily expand the game by editing `linux_commands.json and kali_commands.json`.

Each command follows this structure:

```json
{
  "cmd": "nmap",
  "desc": "Scan a target for open ports",
  "category": "recon",
  "explanation": "Network scanning tool used to discover hosts and services.",
  "usage": "nmap [options] target",
  "examples": ["nmap 192.168.1.1", "nmap -sS -A 192.168.1.1"]
}
```

---

## 🎯 Learning Philosophy

This project is built around:

* **Active Recall** → You must recognize the correct command
* **Immediate Feedback** → Learn instantly from mistakes
* **Repetition with Variation** → Randomized questions improve retention
* **Gamification** → Progression keeps engagement high

---

## ⚠️ Disclaimer

This project is for **educational purposes only**.

* Do not use penetration testing tools on systems you do not own or have permission to test
* Always follow ethical and legal guidelines

---

## 🔮 Future Ideas

* Adaptive difficulty system
* Scenario-based challenges (CTF style)
* Timed rounds / speed mode
* Web-based version
* Multiplayer / leaderboard

---

## 🏆 Final Note

This is more than a game — it’s a **command mastery engine**.

Stay consistent, build streaks, and level up your Linux and cybersecurity skills. 🚀

