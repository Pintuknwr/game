
# Rock-Paper-Scissors Game

Welcome to the Rock-Paper-Scissors game! This is a simple implementation of the classic game using Python. 
The game allows you to play against the computer and see if you can outsmart it.

## Table of Contents

- [Introduction](#introduction)
- [Requirements](#requirements)
- [Installation](#installation)
- [How to Play](#how-to-play)

## Introduction

Rock-Paper-Scissors is a hand game usually played between two people. Each player simultaneously forms one of three shapes with an outstretched hand. 
The possible shapes are rock, paper, and scissors. The winner is determined by the rules:

- Rock crushes Scissors
- Scissors cuts Paper
- Paper covers Rock

This Python script allows you to play this game against the computer. The computer's choice is made randomly, and the winner is determined based on the rules mentioned.

## Requirements

- Python 3.x
- `random` library (part of the Python Standard Library, no installation required)

## Installation

1. Clone the repository or download the script file.
2. Make sure you have Python 3.x installed on your machine.

```sh
git clone https://github.com/Pintuknwr/game.git
cd rock-paper-scissors
```

## How to Play

1. Open a terminal or command prompt.
2. Navigate to the directory where the `game.py` file is located.
3. Run the script using Python:

   ```sh
   game.py
   ```

4. Follow the on-screen instructions to make your choice (rock, paper, or scissors).
5. The computer will make its choice, and the result of the game will be displayed.

## Code Overview

Here's a brief overview of how the game works:

1. **User Input**: The script prompts the user to enter their choice (rock, paper, or scissors).
2. **Computer Choice**: The computer randomly selects one of the three options using the `random` library.
3. **Determine Winner**: The game logic compares the user's choice and the computer's choice to determine the winner.
4. **Display Result**: The result is displayed to the user, showing both choices and the outcome.

