import numpy as np
import random
from time import sleep


# Creates an empty board
def create_board():
    return np.array([[0, 0, 0],
                    [0, 0, 0],
                    [0, 0, 0]])


# Checks for empty spaces on the board
def possibilities(board):
    empty_spaces = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                empty_spaces.append((i, j))
    return empty_spaces


# Selects a random empty space for the player
def random_place(board, player):
    empty_spaces = possibilities(board)
    if not empty_spaces:
        return board  # No valid moves left, return the board

    current_loc = random.choice(empty_spaces)
    board[current_loc] = player
    return board


# Checks if the player has three marks in a horizontal row
def row_win(board, player):
    for row in range(len(board)):
        win = True
        for col in range(len(board)):
            if board[row][col] != player:
                win = False
                break
        if win:
            return win
    return False


# Checks if the player has three marks in a vertical column
def col_win(board, player):
    for col in range(len(board)):
        win = True
        for row in range(len(board)):
            if board[row][col] != player:
                win = False
                break
        if win:
            return win
    return False


# Checks if the player has three marks in a diagonal
def diag_win(board, player):
    win = True
    # Check the main diagonal
    for i in range(len(board)):
        if board[i][i] != player:
            win = False
            break

    if win:
        return win

    win = True
    # Check the anti-diagonal
    for i in range(len(board)):
        j = len(board) - 1 - i
        if board[i][j] != player:
            win = False
            break

    return win


# Evaluates whether there is a winner or a tie
def evaluate(board):
    winner = 0

    for player in [1, 2]:
        if row_win(board, player) or col_win(board, player) or diag_win(board, player):
            winner = player
            break

    # Check for a tie (all spaces filled and no winner)
    if np.all(board != 0) and winner == 0:
        winner = -1

    return winner


# Main function to start the game
def play_game():
    board = create_board()
    winner = 0
    counter = 1

    print(board)
    sleep(2)

    while winner == 0:
        for player in [1, 2]:
            board = random_place(board, player)
            print(f"Board after {counter} move:")  # Use f-string for clean formatting
            print(board)
            sleep(2)
            counter += 1
            winner = evaluate(board)
            if winner != 0:
                break

    if winner == -1:
        print("It's a Tie!")
    else:
        print(f"Player {winner} Wins!")

    return winner


# Driver Code
print("Winner:", play_game())
