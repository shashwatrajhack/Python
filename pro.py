class ConnectFour:
    def __init__(self):
        self.rows = 6
        self.columns = 7
        self.board = [[' ' for _ in range(self.columns)] for _ in range(self.rows)]
        self.current_player = 'X'

    def print_board(self):
        for row in self.board:
            print('|' + '|'.join(row) + '|')
        print('-' * (self.columns * 2 + 1))

    def drop_piece(self, column):
        if column < 0 or column >= self.columns:
            print("Invalid column. Try again.")
            return False

        for row in reversed(self.board):
            if row[column] == ' ':
                row[column] = self.current_player
                return True

        print("Column is full. Try again.")
        return False

    def check_winner(self):
        # Check horizontal locations for win
        for row in range(self.rows):
            for col in range(self.columns - 3):
                if self.board[row][col] == self.current_player and \
                   self.board[row][col + 1] == self.current_player and \
                   self.board[row][col + 2] == self.current_player and \
                   self.board[row][col + 3] == self.current_player:
                    return True

        # Check vertical locations for win
        for row in range(self.rows - 3):
            for col in range(self.columns):
                if self.board[row][col] == self.current_player and \
                   self.board[row + 1][col] == self.current_player and \
                   self.board[row + 2][col] == self.current_player and \
                   self.board[row + 3][col] == self.current_player:
                    return True

        # Check negatively sloped diagonals
        for row in range(3, self.rows):
            for col in range(self.columns - 3):
                if self.board[row][col] == self.current_player and \
                   self.board[row - 1][col + 1] == self.current_player and \
                   self.board[row - 2][col + 2] == self.current_player and \
                   self.board[row - 3][col + 3] == self.current_player:
                    return True

        # Check positively sloped diagonals
        for row in range(self.rows - 3):
            for col in range(self.columns - 3):
                if self.board[row][col] == self.current_player and \
                   self.board[row + 1][col + 1] == self.current_player and \
                   self.board[row + 2][col + 2] == self.current_player and \
                   self.board[row + 3][col + 3] == self.current_player:
                    return True

        return False

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def play_game(self):
        while True:
            self.print_board()
            try:
                col = int(input(f"Player {self.current_player}, choose a column (0--{self.columns - 1}): "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            if self.drop_piece(col):
                if self.check_winner():
                    self.print_board()
                    print(f"Player {self.current_player} wins!")
                    break
                self.switch_player()
            else:
                print("Invalid move. Try again.")

if __name__ == "__main__":
    game = ConnectFour()
    game.play_game()
