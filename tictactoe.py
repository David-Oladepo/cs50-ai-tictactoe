"""
Tic Tac Toe Player
"""

import copy
import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)

    if x_count == o_count:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    available_actions = set()

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                available_actions.add((i, j))

    return available_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise ValueError("Invalid action")

    new_board = copy.deepcopy(board)
    i, j = action
    new_board[i][j] = player(board)

    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] is not EMPTY:
            return board[i][0]

    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] and board[0][j] is not EMPTY:
            return board[0][j]

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not EMPTY:
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not EMPTY:
        return board[0][2]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True

    for row in board:
        if EMPTY in row:
            return False

    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    game_winner = winner(board)

    if game_winner == X:
        return 1
    elif game_winner == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    current_player = player(board)

    if current_player == X:
        best_score = -math.inf
    else:
        best_score = math.inf

    def max_value(state):
        if terminal(state):
            return utility(state)

        value = -math.inf
        for action in actions(state):
            value = max(value, min_value(result(state, action)))
        return value

    def min_value(state):
        if terminal(state):
            return utility(state)

        value = math.inf
        for action in actions(state):
            value = min(value, max_value(result(state, action)))
        return value

    best_action = None

    for action in actions(board):
        new_board = result(board, action)

        if current_player == X:
            score = min_value(new_board)
            if score > best_score:
                best_score = score
                best_action = action
        else:
            score = max_value(new_board)
            if score < best_score:
                best_score = score
                best_action = action

    return best_action
