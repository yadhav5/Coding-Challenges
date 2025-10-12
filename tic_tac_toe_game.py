board = ["1","2","3","4","5","6","7","8","9"]
player = "X"

def show_board():
    print(board[0]+"|"+board[1]+"|"+board[2])
    print("-+-+-")
    print(board[3]+"|"+board[4]+"|"+board[5])
    print("-+-+-")
    print(board[6]+"|"+board[7]+"|"+board[8])

def check_win():
    wins = [(0,1,2),(3,4,5),(6,7,8),
            (0,3,6),(1,4,7),(2,5,8),
            (0,4,8),(2,4,6)]
    for a,b,c in wins:
        if board[a]==board[b]==board[c]:
            return True
    return False

for turn in range(9):
    show_board()
    move = input(f"Player {player}, choose a spot (1-9): ")
    if move not in board:
        print("Invalid move! Try again.")
        continue
    board[int(move)-1] = player
    if check_win():
        show_board()
        print(f"Player {player} wins!")
        break
    player = "O" if player == "X" else "X"
else:
    show_board()
    print("It's a draw!")