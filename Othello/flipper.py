import sys
#pzl = sys.argv[1]
#color = sys.argv[2]
s=8
n=s*s
colors = ["X","O"] #O=White X=Black
num = [str(x) for x in range(64)]
pzl, color, pos = None, None, 20
def whoseTurn(pzl):
    return (len(white)+len(black))&1
for x in sys.argv[1:]:
    if x in num:
        pos = int(x)
    elif len(x)==1:
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
# def whoseTurn(pzl):
#     return pzl.count(".")&1
def display(pzl):
    [print(pzl[x:x+s]) for x in range(0,n,s)]
    print()
direction = [1,-1,-8,8,-7,-9,9,7]
changes = {1:(0,1), -1:(0,-1), -8:(-1,0), 8:(1,0), -7:(-1, 1), -9:(-1,-1), 9:(1, 1), 7:(1, -1)}
coord = {x:(x//s, x%s) for x in range(64)}
def inBounds(val, direction, row, col):
    if val>-1 and val<64:
        valR = coord[val][0]
        valC = coord[val][1]
        return valR==row and valC==col
def flipper(pzl, color, pos):
    pzl  = pzl[:pos]+color+pzl[pos+1:]
    colorDict[color].add(pos)
    tempx = pos
    xrow = pos//s
    xcol = pos%8
    for z in direction:
        x = tempx
        expectedRow = xrow
        expectedCol = xcol
        tup = changes[z]
        expectedRow += tup[0]
        expectedCol += tup[1]
        posFlips = set()
        if inBounds(x+z, direction, expectedRow, expectedCol):
            if pzl[x+z]==opp:
                x+=z
                expectedRow += tup[0]
                expectedCol += tup[1]
                while pzl[x]==opp and inBounds(x+z, direction, expectedRow, expectedCol):
                    posFlips.add(x)
                    x+=z
                    expectedRow += tup[0]
                    expectedCol += tup[1]
                if pzl[x]==color:
                    for r in posFlips:
                        pzl  = pzl[:r]+color+pzl[r+1:]
                    colorDict[opp]-=posFlips
                    colorDict[color] = colorDict[color].union(posFlips)
    display(pzl)
    print(pzl)
    print("Black Tokens vs White Tokens")
    print(len(colorDict[color]), len(colorDict[opp]))
flipper(pzl, color, pos)