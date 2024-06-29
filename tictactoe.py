# Define a function to print the board
def print_board(board):
  for row in board:
    for space in row:
      print(space, end=" ")
    print()

# Define a function to check if a player has won
def check_win(board, player):
  win_conditions = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
  for condition in win_conditions:
    if all(board[i] == player for i in condition):
      return True
  return False

# Define a function to check if the board is full
def is_board_full(board):
  return all(space != " " for space in board)

# Define a function for player move
def player_move(board, player):
  while True:
    move = int(input(f"Player {player}, enter your move (1-9): ")) - 1
    if 0 <= move <= 8 and board[move] == " ":
      board[move] = player
      return
    else:
      print("Invalid move. Try again.")

# Main game loop
game_board = [" "] * 9
current_player = "X"

while True:
  print_board(game_board)
  player_move(game_board, current_player)

  # Check for win
  if check_win(game_board, current_player):
    print_board(game_board)
    print(f"Player {current_player} wins!")
    break

  # Check for draw
  if is_board_full(game_board):
    print_board(game_board)
    print("It's a draw!")
    break

  # Switch players
  current_player = "O" if current_player == "X" else "X"
