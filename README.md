# Tic-Tac-Toe AI

An unbeatable Tic-Tac-Toe game implemented in Python using the Minimax algorithm.

## Overview

This project implements an artificial intelligence agent that plays Tic-Tac-Toe optimally. The AI evaluates possible game states and chooses moves that maximize its chances of winning while preventing the opponent from winning.

## Features

* Determines the current player based on the board state.
* Identifies all legal moves.
* Validates moves and preserves the original board state.
* Detects winners and terminal game states.
* Evaluates outcomes using a utility function.
* Uses the Minimax algorithm to select optimal moves.

## Technologies

* Python 3
* Minimax algorithm
* Recursion
* Game-state evaluation

## How It Works

The AI explores possible future game states recursively. It assumes both players make optimal decisions and evaluates terminal states as follows:

* **+1:** X wins
* **-1:** O wins
* **0:** The game ends in a draw

The algorithm selects the best available move according to whether it is playing as X or O.

## Run Locally

1. Install Python 3.
2. Clone this repository.
3. Navigate to the project directory.
4. Run:

```bash
python tictactoe.py
```

## Testing

The implementation passed all 31 tests in CS50's `check50` for the Tic-Tac-Toe project and received a `style50` score of 1.00.

## Learning Outcomes

This project strengthened my understanding of adversarial search, recursion, state-space exploration, and decision-making in artificial intelligence.

## Acknowledgment

Developed as part of Harvard University's CS50's Introduction to Artificial Intelligence with Python coursework.
