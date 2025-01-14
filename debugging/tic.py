#!/usr/bin/python3
def print_board(board):
    print("\n")  # Added spacing for better visibility
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < 2:  # Only print separator for first two rows
            print("-" * 9)  # Increased length to match board size

def check_winner(board):
    # Check rows, columns and diagonals
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True, row[0]  # Return winner

    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True, board[0][col]  # Return winner

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True, board[0][0]  # Return winner

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True, board[0][2]  # Return winner

    # Check for draw
    if all(all(cell != " " for cell in row) for row in board):
        return True, "Draw"

    return False, None

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        print(f"Player {current_player}'s turn")

        try:
            row = int(input("Enter row (0, 1, or 2): "))
            col = int(input("Enter column (0, 1, or 2): "))

            # Validate input
            if not (0 <= row <= 2 and 0 <= col <= 2):
                print("Invalid input! Row and column must be between 0 and 2.")
                continue

            if board[row][col] != " ":
                print("That spot is already taken! Try again.")
                continue

            board[row][col] = current_player

            # Check for winner or draw
            game_over, winner = check_winner(board)
            if game_over:
                print_board(board)
                if winner == "Draw":
                    print("It's a draw!")
                else:
                    print(f"Player {winner} wins!")
                break

            # Switch players
            current_player = "O" if current_player == "X" else "X"

        except ValueError:
            print("Invalid input! Please enter numbers only.")
        except IndexError:
            print("Invalid input! Row and column must be between 0 and 2.")

if __name__ == "__main__":
    tic_tac_toe()
