# Tic Tac Toe Game
# Player vs AI Implementation

def create_board():
    return [[' ' for _ in range(3)] for _ in range(3)]

def display_board(board):
    print("\n   0   1   2")
    print("  -----------")
    for i, row in enumerate(board):
        print(f"{i} | {' | '.join(row)} |")
        print("  -----------")
    print()

def get_player_move(player, board):
    while True:
        try:
            row = int(input(f"Player {player}, enter row (0-2): "))
            col = int(input(f"Player {player}, enter column (0-2): "))

            if 0 <= row <= 2 and 0 <= col <= 2:
                if board[row][col] == ' ':
                    return row, col
                else:
                    print("That spot is already taken! Try again.")
            else:
                print("Row and column must be between 0 and 2. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def check_win(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)): # Main diagonal
        return True
    if all(board[i][2-i] == player for i in range(3)): # Anti-diagonal
        return True
    return False

def check_draw(board):
    for row in board:
        if ' ' in row: # If any empty space exists, it's not a draw yet
            return False
    return True # Board is full, and if check_win was false, it's a draw

def play_game():
    board = create_board()
    current_player = 'X'
    game_over = False
    
    print("Welcome to Tic-Tac-Toe!")

    while not game_over:
        display_board(board)
        row, col = get_player_move(current_player, board)
        
        board[row][col] = current_player # Apply the move

        if check_win(board, current_player):
            display_board(board)
            print(f"Congratulations, Player {current_player} wins!")
            game_over = True
        elif check_draw(board):
            display_board(board)
            print("It's a draw!")
            game_over = True
        else:
            # Switch player
            current_player = 'O' if current_player == 'X' else 'X'

    # Ask to play again
    while True:
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again in ['yes', 'y']:
            print("\n--- Starting a new game ---")
            play_game() # Recursively call to start a new game
            break # Exit this loop after starting a new game
        elif play_again in ['no', 'n']:
            print("Thanks for playing!")
            break
        else:
            print("Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    play_game()
