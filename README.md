# Tic-Tac-Toe AI — Minimax Algorithm

An interactive Tic-Tac-Toe game featuring an AI opponent that uses the **Minimax algorithm** to choose optimal moves. This project demonstrates adversarial search, game-state evaluation, and decision-making in artificial intelligence.

## Play Online

**[Play Tic-Tac-Toe AI](https://david-oladepo.github.io/cs50-ai-tictactoe/)**

Play as X against the AI, which plays as O. The browser version requires no installation.

## Features

* Human vs. AI gameplay
* Minimax-based move selection
* Optimal AI decision-making
* Interactive browser interface
* Game status and score tracking
* New Game and Reset Scores controls
* Python implementation using Pygame

## How the AI Works

The AI uses the Minimax algorithm to evaluate possible future game states and select a move that maximizes its outcome, assuming the opponent also plays optimally.

* **AI win:** utility of +1
* **Draw:** utility of 0
* **Human win:** utility of -1

The algorithm explores possible moves recursively and chooses the best available move. With correct implementation, the AI should never lose.

## Run the Python Version Locally

### Requirements

* Python 3
* pip

### Installation

Clone the repository:

```bash
git clone https://github.com/David-Oladepo/cs50-ai-tictactoe.git
cd cs50-ai-tictactoe
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Run the game:

```bash
python runner.py
```

If your system uses `python3`, run `python3 runner.py` instead.

Ensure `OpenSans-Regular.ttf` remains in the project directory because the Python interface uses this font.

## Project Structure

* `tictactoe.py` — game logic and Minimax AI
* `runner.py` — Python game interface
* `index.html` — browser-playable game
* `requirements.txt` — Python dependencies
* `OpenSans-Regular.ttf` — font used by the Python interface

## Learning Outcomes

This project explores:

* Adversarial search and game theory fundamentals
* Recursive algorithms and utility functions
* State-space exploration
* AI decision-making under optimal play
* Building and publishing a browser-based application

## Acknowledgements

Developed as part of the Harvard CS50's Introduction to Artificial Intelligence with Python coursework.

## Author

**David Oladepo**

GitHub: [@David-Oladepo](https://github.com/David-Oladepo)
