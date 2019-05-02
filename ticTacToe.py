#create dictionary
theBoard = {
    'topLeft': '', 'topMiddle': '', 'topRight': '',
    'middleLeft': '', 'middleMiddle': '', 'middleRight': '',
    'bottomLeft': '', 'bottomMiddle': '', 'bottomRight': ''
    }

#print the board
def printBoard(board):
    print (board['topLeft'] + '|' + board['topMiddle'] + '|' + board['topRight'])
    print(board['middleLeft'] + '|' + board['middleMiddle'] + '|' + board['middleRight'])
    print(board['bottomLeft'] + '|' + board['bottomMiddle'] + '|' + board['bottomRight'])

turn = 'X'
for i in range (9):
    printBoard(theBoard)
    print('Turn for ' + turn + '\n\n')
    move = input('Move on which space?  ')
    theBoard[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'

printBoard(theBoard)
