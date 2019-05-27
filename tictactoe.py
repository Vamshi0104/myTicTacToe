#function to display the board...
def display_board(board):
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    
#function based on user's input...
def player_input():
    marker = ''
    
    while not (marker == 'X' or marker == 'O'):
        print('Hey!!',player1)
        marker = input('Do you want to be X or O? ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')
    
#function defining the position on the board
def place_marker(board, marker, position):
    board[position] = marker
#function to check the status of winning probability of user...
def win_check(board,mark):    
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or
    (board[4] == mark and board[5] == mark and board[6] == mark) or
    (board[1] == mark and board[2] == mark and board[3] == mark) or 
    (board[7] == mark and board[4] == mark and board[1] == mark) or 
    (board[8] == mark and board[5] == mark and board[2] == mark) or 
    (board[9] == mark and board[6] == mark and board[3] == mark) or
    (board[7] == mark and board[5] == mark and board[3] == mark) or
    (board[9] == mark and board[5] == mark and board[1] == mark))

#function where randomly Player 1 or Player 2 can start the Game...
import random
def choose_first():
    if random.randint(0, 1) == 0:
        return player2
    else:
        return player1
    
# function to check whether the board is filled or not...
def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

#function which allows user choice to place either 'X' or 'O' on the board...
def player_choice(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))
        
    return position

# function if user want to play the Game Again...
def replay():
    
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')

# function to check the space available(blocks) in the board
def space_check(board, position):
    
    return board[position] == ' '

# Game prime code(Looping) starts here :)
print('Welcome to Tic Tac Toe!!')
player1=input('Enter Player_1 name:')
player2=input('Enter Player_2 name:')
while True:
    # Resetting the board
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' Will go First.')
    
    play_game = input('Are you Ready to Play? Enter Yes or No.')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn ==player1:
            # Player1's turn.
            
            display_board(theBoard)
            print(player1,"It's your turn!!")
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Hooray!!',player1,'has Won the Game!!')
                game_on = False
            else:
                if full_board_check(theBoard):#checking whether 
                    display_board(theBoard)
                    print('The Game is a Draw!')
                    break
                else:
                    #Comes the chance for Player2
                    turn = player2
                    
#Quite opposite to if block part here comes the chance for another player who didnt start the game initially...
        else:
            # Player2's turn if the Player 1 started initially the game.
            
            display_board(theBoard)
            print(player2,"It's your turn!!")
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print( 'Hooray!!',player2,'has Won the Game!!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The Game is a Draw!')
                    break
                else:
                   #Comes the chance for Player1 
                    turn =player1
                    
    if not replay():
        break



