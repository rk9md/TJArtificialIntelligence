import sys, time, random
#pzl = sys.argv[1]
#color = sys.argv[2]
evilSet = {"B7", "B8", "A7", "B1", "A2", "B2", "G2", "G1", "H2", "G8", "G7", "H7"}
evilSet = {"B7", "B8", "A7", "B1", "A2", "B2", "G2", "G1", "H2", "G8", "G7", "H7"}
evilList = [*evilSet]
corners = ["A8", "A1", "H1", "H8"]
evilDict = {evilList[x]:corners[x//3] for x in range(len(evilList))}

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
#pzl = "....................XO.....XXO....XOOOX........................."
pzl = pzl.upper()
#color = "O"
color = color.upper()

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


# def bestMove(legal):   #Win rate = 57.5%
#     maxi = 0
#     maxPos = -1
#     if legal:
#         for x in legal:
#             if len(legal[x])>maxi:
#                 maxi = len(legal[x])
#                 maxPos = x
#     return maxPos
# def bestMove(legal):   #Win rate = 57.5%
#     maxi = 0
#     maxPos = -1
#     if legal:
#         for x in legal:
#             if len(legal[x])>maxi:
#                 maxi = len(legal[x])
#                 maxPos = x
#     return maxPos

# def bestMove(legal):    #63
#     maxi = 0
#     maxPos = -1
#     if legal:
#         for x in legal:
#             alpha = numToAlpha(x)
#             if alpha in {"H8", "H1", "A8", "A1"}:
#                 return x
#             if alpha[0]=="H" or alpha[0]=="A" or alpha[1]=="1" or alpha[1]=="8":
#                 return x
#             if len(legal[x])>maxi:
#                 maxi = len(legal[x])
#                 maxPos = x
#     return maxPos


# def bestMove(legal):
#     maxi = 0
#     maxPos = -1
#     if legal:
#         for x in legal:
#             alpha = numToAlpha(x)
#             if alpha in {"H8", "H1", "A8", "A1"}:
#                 return x
#             if alpha[0]=="H" or alpha[0]=="A" or alpha[1]=="1" or alpha[1]=="8":
#                 return x
#     return list(legal)[random.randint(0, len(legal)-1)]

# def bestMove(legal):    #78
#     maxi = 0
#     maxPos = -1
#     if legal:
#         for x in legal:
#             alpha = numToAlpha(x)
#             val = len(legal[x])
#             if alpha in {"H8", "H1", "A8", "A1"}:
#                 val+=3
#             if val>maxi:
#                 maxi = val
#                 maxPos = x
#     return maxPos

# def bestMove(legal, pzl, color):    #79
#     maxi = 0
#     maxPos = None
#     if legal:
#         for x in legal:
#             postpzl = pzl
#             alpha = numToAlpha(x)
#             val = len(legal[x])
#             if alpha not in evilSet:
#                 if alpha in {"H8", "H1", "A8", "A1"}:
#                     return x
#                 if len({"H", "A", "8", "1"}|set(alpha))==4:
#                     for r in legal[x]:
#                         postpzl  = postpzl[:r]+color+postpzl[r+1:]
#                     passed = [True, True]
#                     if alpha[0] in {"H", "A"}:
#                         newx = x
#                         while newx<64:
#                             if postpzl[newx]!=color:
#                                 passed[0] = False
#                                 break
#                             newx+=8
#                         newx = x
#                         while newx>-1:
#                             if postpzl[newx]!=color:
#                                 passed[1] = False
#                                 break
#                             newx-=8
#                     else:
#                         newx = x
#                         row = newx//8
#                         while row==newx//8:
#                             if postpzl[newx]!=color:
#                                 passed[0] = False
#                                 break
#                             newx+=1
#                         newx = x
#                         while newx>-1 and row==newx//8:
#                             if postpzl[newx]!=color:
#                                 passed[1] = False
#                                 break
#                             newx-=1
#                     if passed[0] or passed[1]:
#                         return x
#                 elif (alpha=="G7" and pzl[alphaToNum("H8")]==color) or (alpha=="G2" and pzl[alphaToNum("H1")]==color) or (alpha=="B7" and pzl[alphaToNum("A8")]==color) or (alpha=="B2" and pzl[alphaToNum("A1")]==color):
#                     return x 
#                 elif val>maxi and alpha not in {"G7", "G2", "B2", "B7"}:
#                     maxi = val
#                     maxPos = x
#     if maxPos:
#         return maxPos
#     else:
#         return list(legal)[random.randint(0, len(legal)-1)]

# def bestMove(legal, pzl, color):    #63
#     maxi = 0
#     maxPos = None
#     if legal:
#         for x in legal:
#             alpha = numToAlpha(x)
#             val = len(legal[x])
#             if alpha not in {"G7", "G2", "B2", "B7"}:
#                 if alpha in {"H8", "H1", "A8", "A1"}:
#                     return x
#                 if val>maxi:
#                     maxi = val
#                     maxPos = x
#     if maxPos:
#         return maxPos
#     else:
#         for x in legal:
#             alpha = numToAlpha(x)
#             if pzl[alphaToNum(evilDict[alpha])]==color:
#                 return x
#     return list(legal)[random.randint(0, len(legal)-1)] 

def bestMove(legal, pzl, color):
    maxi = 0
    maxPos = None
    listLegal = list(legal)
    if legal:
        random.shuffle(listLegal)
        for x in listLegal:
            alpha = numToAlpha(x)
            val = len(legal[x])
            if alpha not in evilSet:
                if alpha in {"H8", "H1", "A8", "A1"}:
                    return x
                if len({"H", "A", "8", "1"}|set(alpha))==5:
                    postpzl = pzl
                    newx=x
                    for r in legal[x]:
                        postpzl  = postpzl[:r]+color+postpzl[r+1:]
                    passed = [True, True]
                    if alpha[0] in {"H", "A"}:
                        while newx!=63 and newx!=56:
                            if postpzl[newx]!=color:
                                passed[0] = False
                                break
                            newx+=8
                        while newx!=0 and newx!=7:
                            if postpzl[newx]!=color:
                                passed[0] = False
                                break
                            newx-=8
                    if alpha[1] in {"8", "1"}:
                        while newx!=7 and newx!=63:
                            if postpzl[newx]!=color:
                                passed[1] = False
                                break
                            newx+=1
                        while newx!=0 and newx!=56:
                            if postpzl[newx]!=color:
                                passed[1] = False
                                break
                            newx-=1
                    if passed[0] or passed[1]:
                        return x
                elif val>maxi:
                    maxi = val
                    maxPos = x
            
    if maxPos:
        return maxPos
    else:
        for x in listLegal:
            alpha = numToAlpha(x)
            if alpha not in evilSet:
                return x
            if pzl[alphaToNum(evilDict[alpha])]==color:
                return x
    return list(legal)[random.randint(0, len(legal)-1)]

legal = legalMoves(pzl, color)
bestChoice = bestMove(legal, pzl, color)
print(bestChoice)