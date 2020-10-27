import sys, time, msvcrt
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


pzl, human, pos = None, None, []
for x in sys.argv[1:]:
    if x in num:
        pos.append(int(x))
    elif len(x)==1:
        human = x
    else:
        pzl = x.upper()
if not pzl:
    pzl = "...........................OX......XO..........................."
white = {x for x in range(64) if pzl[x]=="O"}
black = {x for x in range(64) if pzl[x]=="X"}
if not human:
    human = colors[whoseTurn(pzl)]
    comp = ({*colors}-{human}).pop()
    color = human
    opp = comp
elif human==human.upper():
    human = human.upper()
    comp = ({*colors}-{human}).pop()
    color = human
    opp = comp
else:
    human = human.upper()
    comp = ({*colors}-{human}).pop()
    color = colors[whoseTurn(pzl)]
    opp = ({*colors}-{color}).pop()

#pzl = "....................XO.....XXO....XOOOX........................."

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
passes = 0
moves = []
early = False
print("Type -1 to end game early")
display(pzl)
while "." in pzl and passes!=-2:
    print()
    poss = legalMoves(pzl, color)
    if not poss:
        passes-=1
        print("No possible moves. Pass.")
    else:
        passes=0
        letter, number = "", -1
        if color==human:
            timeout = 80
            print("Your Move:",end=" ")   
            startTime = time.time()
            number, letter = None, None
            timeLeft = True
            while timeLeft:
                if msvcrt.kbhit():
                    inp = msvcrt.getch()
                    inp = str(inp)
                    letter = inp[2].upper()
                    break
                if time.time() - startTime > timeout:
                    timeLeft = False
            while timeLeft:
                if msvcrt.kbhit():
                    inp = msvcrt.getch()
                    inp = str(inp)
                    number = inp[2]
                    break
                if time.time() - startTime > timeout:
                    timeLeft = False
            if letter=="-" and number=="1":
                early = True
                print("-1")
                break
            if number and letter and number in num and letter in alpha:
                alphaNum = alphaDict[letter]
                placement = alphaToNum(letter+number)
                if placement not in poss:
                    print("Invalid. Randomly assigning move for player. Move:", end=" ")
                    placement = set(poss).pop()
            else:
                print("Invalid. Randomly assigning move for player. Move:", end=" ")
                placement = set(poss).pop()
        else:
            print("Computer's move:", end=" ")
            placement = set(poss).pop()
     
        print(numToAlpha(placement))
        pzl = flipper(pzl, color, placement)
        moves.append(str(placement))
    display(pzl)
    print(pzl)
    print("Black Tokens vs White Tokens")
    print(len(black), len(white))
    color, opp = opp, color
    startTime = time.time()
    while time.time() - startTime<2:
        k = True
if early:
    print("Game ended early")
else:
    if len(black)>len(white):
        print("Black Wins!")
    elif len(black)<len(white):
        print("White Wins!")
    else:
        print("Tie!")
print(" ".join(moves))