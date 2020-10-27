import sys, time, msvcrt
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
def emptySpacesStr(pzl):
    return [str(x) for x in range(len(pzl)) if pzl[x]=="."] 

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



#pzl = "."*n
#pzl = "XOOX....."
def nextMove(pzl, who):
    if not validBoard(pzl):
        print("Invalid Board")
        return -1
    elif gameOver(pzl):
        print("Game is already finished")
        return 10
    else:
        #who = whoseTurn(pzl)

        g,b,t = partitionMoves(pzl, who, len(emptySpaces(pzl)))
        for x in [g,t,b]:
            if x:
                return x.pop()

pzl = None
human = None
for x in sys.argv[1:]:
    if len(x)==1:
        x = x.upper()
        if x == "X":
            human = 0
        else:
            human = 1
        comp = 1-human
    else:
        pzl = x.upper()

if not pzl:
    pzl= "........."
if human==None:  #MAKE COMPUTER WHO IS THE NEXT MOVE
    comp = whoseTurn(pzl)
    human = 1-comp



turn = whoseTurn(pzl)
#print(turn==human)
if validBoard(pzl):

    if not gameOver(pzl):
        while True:
            display(pzl)
            print()
            placement = 0
            if turn==human:
                print("Your Move:",end=" ", flush=True)
                timeout = 80
                startTime = time.time()
                poss = emptySpacesStr(pzl)
                
                while True:
                    if msvcrt.kbhit():
                        inp = msvcrt.getch()
                        inp = str(inp)
                        placement = inp[2]
                        if placement in poss:
                            placement =int(placement)
                            print(placement)
                            break
                        else:
                            print("\nInvalid. Try another spot. Move:", end=" ", flush=True)
                    elif time.time() - startTime > timeout:
                        placement = nextMove(pzl, turn)
                        print(placement)
                        print("Time up! Automatically assigning player's move")
                        break
            else:
                print("Computer's move:", end=" ", flush=True)
                placement = nextMove(pzl,turn)
                print(placement)
            pzl = pzl[:placement]+sym[turn]+pzl[placement+1:]
            if gameOver(pzl):
                display(pzl)
                print(sym[turn]+" has won the game!")
                break
            if "." not in pzl:
                display(pzl)
                print("The game ends in a tie!")
                break
            turn = 1-turn
    else:
        print("Game already finished")
else:
    print("Invalid board entered")
