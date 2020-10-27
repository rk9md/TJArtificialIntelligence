import sys
s=8
n=s*s


def whoseTurn(pzl):
    return (len(white)+len(black))&1

def display(pzl):
    [print(pzl[x:x+s]) for x in range(0,n,s)]
    print()

colors = ["X","O"] #O=White X=Black
num = [str(x) for x in range(64)]
pzl, color= None, None
for x in sys.argv[1:]:
    if len(x)==1:
        color = x
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

opp = ({*colors}-{color}).pop()
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
legal = legalMoves(pzl, color)
# for x in legal:
#     pzl = pzl[:x]+"*"+pzl[x+1:]
print(pzl)
print("Possible Moves for Token "+color, end=" ")
print(set(legal))