import sys
#pzl = sys.argv[1]
#color = sys.argv[2]
s=8
n=s*s
colors = ["X","O"] #O=White X=Black
num = [str(x) for x in range(64)]
pzl, color= None, None
def whoseTurn(pzl):
    return (len(white)+len(black))&1
for x in sys.argv[1:]:
    if len(x)==1:
        color = x
    else:
        pzl = x
if not pzl:
    pzl = "...........................XO......OX..........................."
white = {x for x in range(64) if pzl[x]=="O"}
black = {x for x in range(64) if pzl[x]=="X"}
if not color:
    color = colors[whoseTurn(pzl)]
#pzl = "....................XO.....XXO....XOOOX........................."
pzl = pzl.upper()
#color = "O"
color = color.upper()

opp = ({*colors}-{color}).pop()
white = {x for x in range(64) if pzl[x]=="O"}
black = {x for x in range(64) if pzl[x]=="X"}
colorDict = {"O":white, "X":black}
oppSet = colorDict[opp]
def display(pzl):
    [print(pzl[x:x+s]) for x in range(0,n,s)]
    print()
def whoseTurn(pzl):
    return (len(white)+len(black))&1    
direction = [1,-1,-8,8,-7,-9,9,7]
changes = {1:(0,1), -1:(0,-1), -8:(-1,0), 8:(1,0), -7:(-1, 1), -9:(-1,-1), 9:(1, 1), 7:(1, -1)}
coord = {x:(x//s, x%s) for x in range(64)}
def inBounds(val, direction, row, col):
    if val>-1 and val<64:
        valR = coord[val][0]
        valC = coord[val][1]
        return valR==row and valC==col
        # if direction==1 or direction==-1:
        #     return valR==row
        # elif direction==8 or direction==-8:
        #     return True
        # else:
        #     return valR
    return False
def legalMoves(pzl, colorMove):
    moves = set()
    for x in colorDict[colorMove]:
        tempx = x
        xrow = x//s
        xcol = x%8
        for z in direction:
            x = tempx
            expectedRow = xrow
            expectedCol = xcol
            tup = changes[z]
            expectedRow += tup[0]
            expectedCol += tup[1]
            if inBounds(x+z, direction, expectedRow, expectedCol):
                if pzl[x+z]==opp:
                    x+=z
                    expectedRow += tup[0]
                    expectedCol += tup[1]
                    while pzl[x]==opp and inBounds(x+z, direction, expectedRow, expectedCol):
                        x+=z
                        expectedRow += tup[0]
                        expectedCol += tup[1]
                    if pzl[x]==".":
                        moves.add(x)
    return moves
#display(pzl)
legal = legalMoves(pzl, color)
for x in legal:
    pzl = pzl[:x]+"*"+pzl[x+1:]
display(pzl)
print(legal)