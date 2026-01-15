# Wordle - Python

An interactive **Wordle** game in Python. Guess the mystery word in 7 attempts!

## 📋 Description

This project is an implementation of the popular **Wordle** game in the command line. The goal is to guess a word in a maximum of 7 attempts. With each attempt, letters are colored to indicate:

- 🟩 **Green** : letter is in the correct position
- 🟨 **Orange** : letter is in the word but in the wrong position
- ⬜ **Gray** : letter is not in the word

## 🚀 Quick Start

### Requirements

- Python 3.x
- No external dependencies

### Installation

1. Clone or download this project
2. Navigate to the project directory:

```bash
cd python-training_exercises
```

### Usage

Launch the game with:

```bash
python3 wordle.py
```

The game will display the number of remaining attempts and ask for your guess. Enter a word and press Enter to submit your answer.

## 📁 Project Structure

- `wordle.py` : main game script
- `wordlist.txt` : list of available words for the game
- `README.md` : this file

## 🎮 How to Play

1. Launch the game
2. Guess the hidden word in a maximum of 7 attempts
3. Observe the colors to refine your hypotheses:
   - Green letters : correct position ✓
   - Orange letters : wrong position
   - Gray letters : not in the word

4. Find the word before your attempts run out!

## 📝 License

This project is a Python training exercise.
