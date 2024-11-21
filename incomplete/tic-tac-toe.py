import os,sys
board = {'LT' : ' ', 'LM' : ' ', 'LB' : ' ',
         'MT' : ' ', 'MM' : ' ', 'MB' : ' ',
         'RT' : ' ', 'RM' : ' ', 'RB' : ' '}
def printboard(board):
    print(board['LT'] + '|' + board['MT'] + '|' + board['RT'])
    print('-+-+-')
    print(board['LM'] + '|' + board['MM'] + '|' + board['RM'])
    print('-+-+-')
    print(board['LB'] + '|' + board['MB'] + '|' + board['RB'])

def inp():
    move = input("Enter your move: ").upper()
    if move not in board.keys():
        print('Pick another move')
        return inp()  # Return the result of the recursive call
    else:
        return move
        
try:    
    def Main():
        turn = 'X'
        move = 'LT'
        for i in range(9):
            printboard(board)
            print('Turn for ' + turn + ' input the move.\n')
            move = inp()
            board[move] = turn
            os.system('cls')
            if turn == 'X':
                turn = 'O'
            else:
                turn = 'X'
        
    Main()
except KeyboardInterrupt:
    sys.exit()
       