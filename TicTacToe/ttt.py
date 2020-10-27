import sys
side = 3
n = side**2
turnDecider = n&1
def validBoard(pzl):
    return pzl.count("X")-pzl.count("O") in {1,0} and len(pzl)==9
def whoseTurn(pzl):
    return 1-pzl.count(".")&1

def display(pzl):
    [print(pzl[x:x+side]) for x in range(0,n,side)]

def emptySpaces(pzl):
    return [x for x in range(len(pzl)) if pzl[x]=="."]    
rowsColsDiags = [{0,1,2},{3,4,5}, {6,7,8}, {0,3,6},{1,4,7}, {2,5,8}, {0,4,8}, {2,4,6}]
listRowsColsDiags = [[*x] for x in rowsColsDiags]
#^^needs to be changed for any num of spaces
sym = ["X", "O"]
def gameOver(pzl): #needs to be changed for any num of spaces
    for x in listRowsColsDiags:
        if pzl[x[0]]==pzl[x[1]]==pzl[x[2]]!=".":
            return True
    return False
    #return sum([pzl[x[0]]==pzl[x[1]]==pzl[x[2]]!="." for x in listRowsColsDiags])

def partitionMoves(pzl, turn, numSpaces):
    if gameOver(pzl):
        return set(),{""},set()
    if numSpaces==0:
        return set(),set(),{""}
    good,bad,tie = set(),set(),set()
    for x in emptySpaces(pzl):
        newPzl = pzl[:x]+sym[turn]+pzl[x+1:]
        tempGood, tempBad, tempTie = partitionMoves(newPzl,1-turn, numSpaces-1)
        if tempGood:
            bad.add(x)
        elif tempTie:
            tie.add(x)
        else:
            good.add(x)
    return good, bad, tie    

pzl = sys.argv[1].upper()
#pzl = "."*n
#pzl = "XOOX....."
if not validBoard(pzl):
    print("Invalid Starting Board")
elif gameOver(pzl):
    print("Game is already finished")
else:
    who = whoseTurn(pzl)
    display(pzl)
    g,b,t = partitionMoves(pzl, who, len(emptySpaces(pzl)))
    if not g:
        g = " None "
    if not b:
        b = " None "
    if not t:
        t = " None "
    print("Good moves: "+str(g)[1:-1])
    print("Bad moves: "+str(b)[1:-1])
    print("Tie moves: "+str(t)[1:-1])