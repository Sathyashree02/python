def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    for row in board:
        if all([cell == player for cell in row]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2-i] == player for i in range(3)]):
        return True
    return False

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"
    
    for _ in range(9):
        print_board(board)
        while True:
            try:
                row, col = map(int, input(f"Player {player}, enter row and column (0, 1, 2): ").split())
                if row in [0, 1, 2] and col in [0, 1, 2]:
                    if board[row][col] == " ":
                        board[row][col] = player
                        break
                    else:
                        print("Cell is already occupied. Try again.")
                else:
                    print("Invalid input. Please enter 0, 1, or 2.")
            except ValueError:
                print("Invalid input. Please enter two numbers separated by a space.")
        
        if check_winner(board, player):
            print_board(board)
            print(f"Player {player} wins!")
            return
        player = "O" if player == "X" else "X"
    
    print_board(board)
    print("It's a draw!")

tic_tac_toe()