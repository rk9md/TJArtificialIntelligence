import sys, time, msvcrt, random

def bestMove(legal):    #63
    maxi = 0
    maxPos = -1
    if legal:
        for x in legal:
            alpha = numToAlpha(x)
            val = len(legal[x])
            if alpha in {"H8", "H1", "A8", "A1"}:
                val+=3
            if val>maxi:
                maxi = val
                maxPos = x
    return maxPos

def oppMove(legal):
    #return list(legal)[random.randint(0, len(legal)-1)]
    return bestMove(legal)

#pzl = sys.argv[1]
#color = sys.argv[2]
s=8
n=s*s
colors = ["X","O"] #O=White X=Black
num = {str(x) for x in range(64)}
aStr = "ABCDEFGH" 
alphaDict = {z:aStr.index(z) for z in aStr}
alpha = set(aStr)

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
# pzl = "...........................OX......XO..........................." 
# human  = colors[random.randint(0,1)]
# comp = ({*colors}-{human}).pop()
# color = human
# opp = comp

# white = {x for x in range(64) if pzl[x]=="O"}
# black = {x for x in range(64) if pzl[x]=="X"}
# colorDict = {"O":white, "X":black}

   
# direction = [1,-1,-8,8,-7,-9,9,7]
# changes = {1:(0,1), -1:(0,-1), -8:(-1,0), 8:(1,0), -7:(-1, 1), -9:(-1,-1), 9:(1, 1), 7:(1, -1)}
# coord = {x:(x//s, x%s) for x in range(64)}

def inBounds(val, direction, row, col):
    if val>-1 and val<64:
        valR = coord[val][0]
        valC = coord[val][1]
        return valR==row and valC==col
    return False

def legalMoves(pzl, colorMove):
    moves = {}
    for x in colorDict[colorMove]:
        tempx = x
        xrow = x//s
        xcol = x%8
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

def flipper(pzl, color, pos):
    legal = legalMoves(pzl, color)
    if pos in legal:
        changeSet = legal[pos]
        changeSet.add(pos)
        for r in changeSet:
            pzl  = pzl[:r]+color+pzl[r+1:]
        colorDict[opp]-=changeSet
        colorDict[color]|=changeSet
    else:
        print("Move is Invalid")

    return pzl

firstSecond = [0,0]
scoreBoard = [0, 0, 0]
games = 1000
if len(sys.argv)>1:
    games = int(sys.argv[1])
for x in range(games):
    pzl = "...........................OX......XO..........................." 
    human  = colors[random.randint(0,1)]
    comp = ({*colors}-{human}).pop()
    if human=="X":
        color = human
        opp = comp
        firstSecond[0]+=1
    else:
        color = comp
        opp = human
        firstSecond[1]+=1
    white = {x for x in range(64) if pzl[x]=="O"}
    black = {x for x in range(64) if pzl[x]=="X"}
    colorDict = {"O":white, "X":black}

    
    direction = [1,-1,-8,8,-7,-9,9,7]
    changes = {1:(0,1), -1:(0,-1), -8:(-1,0), 8:(1,0), -7:(-1, 1), -9:(-1,-1), 9:(1, 1), 7:(1, -1)}
    coord = {x:(x//s, x%s) for x in range(64)}

    passes = 0
    moves = []
    early = False
    while "." in pzl and passes!=-2:
        poss = legalMoves(pzl, color)
        if not poss:
            passes-=1
        else:
            passes=0
            letter, number = "", -1
            if color==human:
                placement = bestMove(poss)
            else:
                placement = oppMove(poss)
            pzl = flipper(pzl, color, placement)
            moves.append(placement)
        color, opp = opp, color

    if len(black)>len(white):
        if human == "X":
            scoreBoard[0]+=1
        else:
            scoreBoard[1]+=1
    elif len(black)<len(white):
        if human == "O":
            scoreBoard[0]+=1
        else:
            scoreBoard[1]+=1
    else:
        scoreBoard[2]+=1
print("Score (Win-Loss-Tie):")
print(scoreBoard)
print(str(scoreBoard[0]/games*100)+"%")
print(firstSecond)