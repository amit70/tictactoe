import random

print '******* TIC TAC TOE************'


def userChoice():
    global p1
    global p2
    choice = raw_input("Enter your choice: X or O ")
    if choice == 'X':
        p1 = 'X'
        p2 = 'O'
    else:
        p1 = 'O'
        p2 = 'X'


def turnSelection():
    l = ['Player_1', 'Player_2']
    return random.choice(l)

def checkInput(str):

    if str == '0' or str == '1' or str == '2' or str == '3' \
            or str == '4' or str == '5' or str == '6'\
            or str == '7' or str == '8' or str == '9':
        return True
    else:
        return False


def userInput(marker):
    boards_pos = ''
    while True:
        if checkInput(boards_pos):
            if board[int(boards_pos)] == ' ':
                board[int(boards_pos)] = marker
                break
            else:
                boards_pos = raw_input('Position already taken. Please enter a different position ')
        else:
            boards_pos = raw_input('Enter board position from 1 - 9 for player %s : ' % (marker))




def printBoard(board):
    print "----------------------------"
    print "    " + board[1] + "    |    " + board[2] + "    |    " + board[3] + "    "
    print "----------------------------"
    print "    " + board[4] + "    |    " + board[5] + "    |    " + board[6] + "    "
    print "----------------------------"
    print "    " + board[7] + "    |    " + board[8] + "    |    " + board[9] + "    "


def checkBoardWon(board, marker):
    if board[1] == board[2] == board[3] == marker or board[4] == board[5] == board[6] == marker or board[7] == board[
        8] == board[9] == marker or board[1] == board[4] == board[7] == marker or board[2] == board[5] == board[
        8] == marker or board[3] == board[6] == board[9] == marker or board[1] == board[5] == board[9] == marker or \
            board[3] == board[5] == board[7] == marker:
        return True
    else:
        return False


def replay():
    return raw_input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')


while True:
    p1 = ''
    p2 = ''
    userChoice()
    print 'PLayer1 will play with %s' % p1
    print 'PLayer2 will play with %s' % p2
    turn = turnSelection()
    print ''
    print '%s will go first' % turn
    board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    printBoard(board)
    matchTie = True
    while board.count(' ') > 1:
        if turn == 'Player_1':
            userInput(p1)
            printBoard(board)
            if checkBoardWon(board, p1):
                matchTie = False
                print 'Player %s Won' % p1
                print 'Player %s Lost' % p2
                break
            else:
                turn = 'Player_2'
        else:
            if board.count(' ') > 1:
                userInput(p2)
                printBoard(board)
                if checkBoardWon(board, p2):
                    matchTie = False
                    print 'Player %s Won' % p2
                    print 'Player %s Lost' % p1
                    break
                else:
                    turn = 'Player_1'

    if matchTie:
        print ''
        print 'Match Tied'

    if not replay():
        break