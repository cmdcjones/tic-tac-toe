# starting game board
board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

player_side = True # True is X, False is O

def display_board(board):
    print("-"*11)
    for row in range(3):
        for col in range(1):
            if row >= 1 and row % 2 != 0:
                print(f' {board[(row * 2) + 1]} | {board[(row * 2) + 2]} | {board[(row * 2) + 3]} ')
            elif row >= 1 and row % 2 == 0:
                print(f' {board[(row * 3)]} | {board[(row * 3) + 1]} | {board[(row * 3) + 2]} ')
            else:
                print(f' {board[row]} | {board[row + 1]} | {board[row + 2]} ')
        print("-"*11)

def player_input(board):
    counted_squares = 0
    for square in board:
        if square == ' ':
            counted_squares += 1
    print(f"There are {counted_squares} squares available.")
    while True:
        if player_side:
            side = 'X'
            action = input(f"{side}'s turn! Choose a square by typing a number!\n> ")
        else:
            side = 'O'
            action = input(f"{side}'s turn! Choose a square by typing a number!\n> ")
        move = legal_move(action)
        if move != None:
            break
    if player_side:
        board[move - 1] = 'X'
    else:
        board[move - 1] = 'O'

def legal_move(move):
    try:
        move = int(move)
        if move < 1 or move > 9:
            print("Please type a number between 1-9!")
            return None
        elif board[move - 1] != ' ':
            print("That square is taken please try another move!")
            return None
        return move
    except:
        print("Please type a number (ex. 123)!")
        return None

def is_board_full(board):
    for square in board:
        if square == ' ':
            return False
    return True

def is_win(board):
    # X win conditions
    if board[0] == 'X' and board[1] == 'X' and board[2] == 'X':
        return True
    elif board[3] == 'X' and board[4] == 'X' and board[5] == 'X':
        return True
    elif board[6] == 'X' and board[7] == 'X' and board[8] == 'X':
        return True
    elif board[0] == 'X' and board[3] == 'X' and board[6] == 'X':
        return True
    elif board[1] == 'X' and board[4] == 'X' and board[7] == 'X':
        return True
    elif board[2] == 'X' and board[5] == 'X' and board[8] == 'X':
        return True
    elif board[0] == 'X' and board[4] == 'X' and board[8] == 'X':
        return True
    elif board[6] == 'X' and board[4] == 'X' and board[2] == 'X':
        return True
    # O win conditions
    elif board[0] == 'O' and board[1] == 'O' and board[2] == 'O':
        return True
    elif board[3] == 'O' and board[4] == 'O' and board[5] == 'O':
        return True
    elif board[6] == 'O' and board[7] == 'O' and board[8] == 'O':
        return True
    elif board[0] == 'O' and board[3] == 'O' and board[6] == 'O':
        return True
    elif board[1] == 'O' and board[4] == 'O' and board[7] == 'O':
        return True
    elif board[2] == 'O' and board[5] == 'O' and board[8] == 'O':
        return True
    elif board[0] == 'O' and board[4] == 'O' and board[8] == 'O':
        return True
    elif board[6] == 'O' and board[4] == 'O' and board[2] == 'O':
        return True

if __name__ == "__main__":
    print("Welcome to Tic Tac Toe!")
    while True:
        display_board(board)
        if is_win(board):
            if player_side:
                winner = 'X'
            else:
                winner = 'O'
            action = input(f"{winner}'s Win! Would you like to play again? (Y/N)\n> ")
            if action.lower() == 'y':
                board =  [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
                player_side = True
                continue
            else:
                exit()
        if is_board_full(board):
            action = input("Draw game! Would you like to play again? (Y/N)\n> ")
            if action.lower() == 'y':
                board =  [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
                player_side = True
                continue
            else:
                exit()
        player_input(board)
        if not is_win(board) and not is_board_full(board):
            player_side = not player_side
