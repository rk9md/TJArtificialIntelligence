import sys, time, random 

s=8
n=s*s
colors = ["X","O"] #O=White X=Black
num = {str(x) for x in range(64)}
aStr = "ABCDEFGH" 
alphaDict = {z:aStr.index(z) for z in aStr}
alpha = set(aStr)
numToRow = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 1, 9: 1, 10: 1, 11: 1, 12: 1, 13: 1, 14: 1, 15: 1, 16: 2, 17: 2, 18: 2, 19: 2, 20: 2, 21: 2, 22: 2, 23: 2, 24: 3, 25: 3, 26: 3, 27: 3, 28: 3, 29: 3, 30: 3, 31: 3, 32: 4, 33: 4, 34: 4, 35: 4, 36: 4, 37: 4, 38: 4, 39: 4, 40: 5, 41: 5, 42: 5, 43: 5, 44:5, 45: 5, 46: 5, 47: 5, 48: 6, 49: 6, 50: 6, 51: 6, 52: 6, 53: 6, 54: 6, 55: 6, 56: 7, 57: 7, 58: 7,59: 7, 60: 7, 61: 7, 62: 7, 63: 7}
numToCol = {0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 0, 9: 1, 10: 2, 11: 3, 12: 4, 13: 5, 14: 6, 15: 7, 16: 0, 17: 1, 18: 2, 19: 3, 20: 4, 21: 5, 22: 6, 23: 7, 24: 0, 25: 1, 26: 2, 27: 3, 28: 4, 29: 5, 30: 6, 31: 7, 32: 0, 33: 1, 34: 2, 35: 3, 36: 4, 37: 5, 38: 6, 39: 7, 40: 0, 41: 1, 42: 2, 43: 3, 44:4, 45: 5, 46: 6, 47: 7, 48: 0, 49: 1, 50: 2, 51: 3, 52: 4, 53: 5, 54: 6, 55: 7, 56: 0, 57: 1, 58: 2,59: 3, 60: 4, 61: 5, 62: 6, 63: 7}

def alphaToNum(pos):
    return (int(pos[1])-1)*8+alphaDict[pos[0]]

def numToAlpha(pos):
    number = pos//8+1
    letter = aStr[pos%8]
    return letter+str(number)

def whoseTurn(pzl):
    return (len(white)+len(black))&1

def display(pzl):
    [print(pzl[x:x+s]) for x in range(0,n,s)]
    print()

pzl, color= None, None
for x in sys.argv[1:]:
    if len(x)==1:
        color = x
    else:
        pzl = x
if not pzl:
    pzl = "...........................OX......XO..........................."
white = {x for x in range(64) if pzl[x]=="O"}
black = {x for x in range(64) if pzl[x]=="X"}
if not color:
    color = colors[whoseTurn(pzl)]

pzl = pzl.upper()

color = color.upper()

opp = ({*colors}-{color}).pop()
white = {x for x in range(64) if pzl[x]=="O"}
black = {x for x in range(64) if pzl[x]=="X"}
colorDict = {"O":white, "X":black}
oppSet = colorDict[opp]

   
direction = [1,-1,-8,8,-7,-9,9,7]
changes = {1:(0,1), -1:(0,-1), -8:(-1,0), 8:(1,0), -7:(-1, 1), -9:(-1,-1), 9:(1, 1), 7:(1, -1)}
#coord = {x:(numToRow[x], numToCol[x]) for x in range(64)}

def inBounds(val, direction, row, col):
    if val>-1 and val<64:
        valR = numToRow[val]
        valC = numToCol[val]
        return valR==row and valC==col
    return False

def legalMoves(pzl, colorMove, black, white):
    moves = {}
    colorDict = {"O":white, "X":black}
    opp = dictEnemy[colorMove]
    for x in colorDict[colorMove]:
        tempx = x
        xrow = numToRow[x]
        xcol = numToCol[x]
        for z in direction:
            x = tempx
            expectedRow = xrow
            expectedCol = xcol
            path = set()
            tup = changes[z]
            expectedRow += tup[0]
            expectedCol += tup[1]
            if inBounds(x+z, direction, expectedRow, expectedCol):
                if pzl[x+z]==opp:
                    x+=z
                    expectedRow += tup[0]
                    expectedCol += tup[1]
                    while pzl[x]==opp and inBounds(x+z, direction, expectedRow, expectedCol):
                        path.add(x)
                        x+=z
                        expectedRow += tup[0]
                        expectedCol += tup[1]
                    if pzl[x]==".":
                        if x not in moves:
                            moves[x] = set()
                        moves[x] = moves[x].union(path)
    return moves

def flipper(npzl, changeSet, ncolor, pos):
    for r in changeSet:
        z = npzl[r]
        npzl  = npzl[:r]+ncolor+npzl[r+1:]
    npzl  = npzl[:pos]+ncolor+npzl[pos+1:]
    return npzl

def bestMove(board, color, black, white):
    return negaMax(board, color, 5, black, white)
def boardEval(board, token):
    periods = 0
    mine = 0
    for x in board:
        if x ==token:
            mine+=1
        if x == ".":
            periods+=1
    return mine - (64-periods-mine)
dictEnemy = {'X':"O", "O":"X"}
tokentoNum = {'X':0, "O":1}

def negaMax(board, token, depth, black, white):
    if depth == 0:
        if token=="X":
            return [len(black)-len(white)]
        else: 
            return [len(white)-len(black)]
    lm = legalMoves(board, token, black, white)
    if not lm:
        nm = negaMax(board, dictEnemy[token], depth -1, black, white)+[-1]
        return [-1*nm[0]]+nm[1:]
    if token=="X":
        nmlist = sorted([negaMax(flipper(board, lm[pos], token, pos), dictEnemy[token], depth-1,  black|lm[pos], white-lm[pos])+[pos] for pos in lm])
    else:
        nmlist = sorted([negaMax(flipper(board, lm[pos], token, pos), dictEnemy[token], depth-1,  black-lm[pos], white|lm[pos])+[pos] for pos in lm])
    best  = nmlist[0]
    return [-1*best[0]] + nmlist[0][1:]



cornerset = {0, 7, 56, 63}
legal = legalMoves(pzl, color, black, white)
cor = set(legal)&cornerset
if cor:
    print(random.choice(list(cor)))  
else:
    print(random.choice(list(legal)))
    bestChoice = bestMove(pzl, color, black, white)
    print(bestChoice)