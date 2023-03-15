#Tic Tac Toe board
def print_board(board):
    print(board[0] + '|' + board[1] + '|' + board[2])
    print('-+-+-')
    print(board[3] + '|' + board[4] + '|' + board[5])
    print('-+-+-')
    print(board[6] + '|' + board[7] + '|' + board[8])

#-----------------------------------------------------------------------------------------------------------------------
#All options to win tic tac toe
def check_win(board, player):
    if board[0] == player and board[1] == player and board[2] == player:
        return True
    elif board[3] == player and board[4] == player and board[5] == player:
        return True
    elif board[6] == player and board[7] == player and board[8] == player:
        return True
    elif board[0] == player and board[3] == player and board[6] == player:
        return True
    elif board[1] == player and board[4] == player and board[7] == player:
        return True
    elif board[2] == player and board[5] == player and board[8] == player:
        return True
    elif board[0] == player and board[4] == player and board[8] == player:
        return True
    elif board[2] == player and board[4] == player and board[6] == player:
        return True
    else:
        return False

#-----------------------------------------------------------------------------------------------------------------------
def tic_tac_toe():
    board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    players = ['\033[33m' + 'O','\033[91m' +  'X']
    turn = 0
    # Loop until the game is won or a tie is reached.
    while True:
        # Print the current state of the board.
        print_board(board)
        # Determine whose turn it is.
        player = players[turn % 2]
        print("It's " + player + "'s turn.")
        # Prompt the player to make a move.
        while True:
            move = input('Enter a number between 1 and 9: ')
            # Validate the player's move input.
            if move.isdigit() and int(move) in range(1, 10):
                if board[int(move) - 1] != 'X' and board[int(move) - 1] != 'O':
                    break
                else:
                    print('That space is already taken.')
            else:
                print('Invalid input. Please enter a number between 1 and 9.')
        # Update the board with the player's move.
        board[int(move) - 1] = player
        # Check if the player has won the game.
        if check_win(board, player):
            print_board(board)
            print(player + ' wins!')
            break
        # Check if the game has resulted in a tie.
        elif all([val != ' ' for val in board]):
            print_board(board)
            print('Tie game!')
            break
        # If neither a win nor a tie has occurred, continue the game with the next player's turn.
        turn += 1
    print('Thanks for playing!')

# Call the main function to start the game.
tic_tac_toe()
