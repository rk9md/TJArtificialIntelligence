import sys, time
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
    #print()

pzl, color, pos = None, None, []
for x in sys.argv[1:]:
    if x in num or len(x)==2:
        pos.append(x.upper())
    elif len(x)==1:
        color = x.upper()
    else:
        pzl = x.upper()
if not pzl:
    pzl = "...........................OX......XO..........................."
white = {x for x in range(64) if pzl[x]=="O"}
black = {x for x in range(64) if pzl[x]=="X"}
if not color:
    color = colors[whoseTurn(pzl)]
#pzl = "....................XO.....XXO....XOOOX........................."
pzl = pzl.upper()
#color = "O"
color = color.upper()
for x,p in enumerate(pos):
    if p in num:
        pos[x] = int(p)
    else:
        pos[x] = alphaToNum(p)
opp = ({*colors}-{color}).pop()
white = {x for x in range(64) if pzl[x]=="O"}
black = {x for x in range(64) if pzl[x]=="X"}
colorDict = {"O":white, "X":black}
oppSet = colorDict[opp]

   
direction = [1,-1,-8,8,-7,-9,9,7]
changes = {1:(0,1), -1:(0,-1), -8:(-1,0), 8:(1,0), -7:(-1, 1), -9:(-1,-1), 9:(1, 1), 7:(1, -1)}
coord = {x:(x//s, x%s) for x in range(64)}

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
    if legal:
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

display(pzl)
print(pzl, end=" ")
print(len(colorDict[color]), len(colorDict[opp]))
for move in range(len(pos)):
    prepzl = pzl
    pzl = flipper(pzl, color, pos[move])
    if prepzl!=pzl:
        print(color+" => "+str(pos[move]))
    else:
        print(color+" Passes")
        color, opp = opp, color
        pzl = flipper(pzl, color, pos[move])
    print()
    display(pzl)
    print(pzl, end=" ")
    print(len(black), len(white))
    color, opp = opp, color
#print("Move summary: "+str(pos)[1:-1])