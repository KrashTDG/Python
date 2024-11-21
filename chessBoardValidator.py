import sys
def chboard():
    chboard={}
    for row in range(1,9):
        for col in 'abcdefgh':
            position = str(row) + str(col)
            chboard[position] = ''
    return chboard
        

chboard = chboard()
def isValidChessBoard(chboard,k,v):
    if k not in chboard.keys():
        return False
    elif v not in {'wknight', 'wqueen', 'wking', 'wbishop', 'wpawn', 'wrook', 
               'bknight', 'bqueen', 'bking', 'bbishop', 'bpawn', 'brook'}:
        return False
    else:
        return True
    

try:
    k = input()
    v = input()
    print(isValidChessBoard(chboard,k,v))
except KeyboardInterrupt:
    sys.exit()