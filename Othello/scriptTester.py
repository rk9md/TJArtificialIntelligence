import sys, time, random
evilSet = {"B7", "B8", "A7", "B1", "A2", "B2", "G2", "G1", "H2", "G8", "G7", "H7"}
evilList = [*evilSet]
corners = ["A8", "A1", "H1", "H8"]
evilDict = {evilList[x]:corners[x//3] for x in range(len(evilList))}
cornerset = {0, 7, 56, 63}
cornerset = {0, 7, 56, 63}
def bestMove(legal, pzl, color):
    maxi = 0
    maxPos = None
    corners = set(legal) & cornerset
    if corners:
        return random.choice([*corners])
    safeedges = set()
    innersquares =  []
    if legal:
        for x in legal:
            alpha = numToAlpha(x)
            val = len(legal[x])
            if alpha not in evilSet:
                # if alpha in {"H8", "H1", "A8", "A1"}:
                #     corners.add(x)
                if len({"H", "A", "8", "1"}|set(alpha))==5:
                    #print("Ajith")
                    postpzl = pzl
                    for r in legal[x]:
                        postpzl  = postpzl[:r]+color+postpzl[r+1:]
                    passed = [True, True]
                    newx = x
                    if alpha[0] in {"H", "A"}:
                        while newx!=63 and newx!=56:
                            if postpzl[newx]!=color:
                                passed[0] = False
                                break
                            newx+=8
                        newx = x
                        while newx!=0 and newx!=7:
                            if postpzl[newx]!=color:
                                passed[0] = False
                                break
                            newx-=8
                        newx = x
                    if alpha[1] in {"8", "1"}:
                        newx = x
                        while newx!=7 and newx!=63:
                            if postpzl[newx]!=color:
                                passed[1] = False
                                break
                            newx+=1
                        newx = x
                        while newx!=0 and newx!=56:
                            if postpzl[newx]!=color:
                                passed[1] = False
                                break
                            newx-=1
                    if passed[0] or passed[1]:
                        safeedges.add(x)
                elif val>maxi:
                    maxi = val
                    innersquares.clear()
                    innersquares.append(x)
                    maxPos = x
                elif val==maxi:
                    #maxi = val
                    innersquares.append(x)
                    #maxPos = x
            
    
    if safeedges:
        return random.choice([*safeedges])
    elif innersquares:
        return innersquares[0]
    else:
        for x in legal:
            alpha = numToAlpha(x)
            if alpha not in evilSet:
                return x
            if pzl[alphaToNum(evilDict[alpha])]==color:
                return x
    return list(legal)[random.randint(0, len(legal)-1)]

# def bestMove(legal, pzl, color):    #79
#     maxi = 0
#     maxPos = None
#     if legal:
#         for x in legal:
#             postpzl = pzl
#             alpha = numToAlpha(x)
#             val = len(legal[x])
#             if alpha in {"H8", "H1", "A8", "A1"}:
#                 return x
#             if len({"H", "A", "8", "1"}|set(alpha))==4:
#                 for r in legal[x]:
#                     postpzl  = postpzl[:r]+color+postpzl[r+1:]
#                 passed = [True, True]
#                 if alpha[0] in {"H", "A"}:
#                     newx = x
#                     while newx<64:
#                         if postpzl[newx]!=color:
#                             passed[0] = False
#                             break
#                         newx+=8
#                     newx = x
#                     while newx>-1:
#                         if postpzl[newx]!=color:
#                             passed[1] = False
#                             break
#                         newx-=8
#                 else:
#                     newx = x
#                     row = newx//8
#                     while row==newx//8:
#                         if postpzl[newx]!=color:
#                             passed[0] = False
#                             break
#                         newx+=1
#                     newx = x
#                     while newx>-1 and row==newx//8:
#                         if postpzl[newx]!=color:
#                             passed[1] = False
#                             break
#                         newx-=1
#                 if passed[0] or passed[1]:
#                     return x
#             elif (alpha=="G7" and pzl[alphaToNum("H8")]==color) or (alpha=="G2" and pzl[alphaToNum("H1")]==color) or (alpha=="B7" and pzl[alphaToNum("A8")]==color) or (alpha=="B2" and pzl[alphaToNum("A1")]==color):
#                 return x 
#             if val>maxi and alpha not in {"G7", "G2", "B2", "B7"}:
#                 maxi = val
#                 maxPos = x
#     if maxPos:
#         return maxPos
#     else:
#         return list(legal)[random.randint(0, len(legal)-1)]

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



myPieces = 0
oppPieces = 0
possTime = 0
totalMoves = 0
possMoves = 0
madeMoves = 0
totalTime = 0
firstSecond = [0,0]
scoreBoard = [0, 0, 0]
games = 1000
if len(sys.argv)>1:
    games = int(sys.argv[1])
#start=time.time()
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
        possStart = time.time()
        poss = legalMoves(pzl, color)
        possTime+=(time.time()-possStart)
        totalMoves+=1
        possMoves +=len(poss)
        if not poss:
            passes-=1
        else:
            passes=0
            letter, number = "", -1
            if color==human:
                start = time.time()
                
                placement = bestMove(poss, pzl, color)
                madeMoves+=1
                totalTime+=(time.time()-start)
            else:
                placement = list(poss)[random.randint(0, len(poss)-1)]
            pzl = flipper(pzl, color, placement)
            moves.append(placement)
        color, opp = opp, color

    if len(black)>len(white):
        if human == "X":
            scoreBoard[0]+=1
            myPieces+=len(black)
            oppPieces+=len(white)
        else:
            scoreBoard[1]+=1
            myPieces+=len(white)
            oppPieces+=len(black)
    elif len(black)<len(white):
        if human == "O":
            scoreBoard[0]+=1
            myPieces+=len(white)
            oppPieces+=len(black)
        else:
            scoreBoard[1]+=1
            myPieces+=len(black)
            oppPieces+=len(white)
    else:
        scoreBoard[2]+=1
print("Score (Win-Loss-Tie):")
print(scoreBoard)
print(str(scoreBoard[0]/games*100)+"%")
print(firstSecond)
print(totalTime/madeMoves)
print(possMoves/totalMoves)
print(possTime/totalMoves)
print(myPieces/(oppPieces+myPieces))
#print((time.time()-start))