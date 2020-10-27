import sys
moves = {0:[1, 4], 1:[0, 2, 5], 2:[1, 3, 6], 3:[2, 7], 4:[0, 5, 8], 5:[1, 4, 6, 9], 6:[2, 5, 7, 10], 7:[3, 6, 11], 8:[4, 9, 12], 9:[5, 8, 10, 13], 10:[6, 9, 11, 14], 11:[7, 10, 15], 12:[8, 13], 13:[9, 12, 14], 14:[10, 13, 15], 15:[11, 14]}
def printstate ( currstate ):
    for r in range (4):
        for c in range (4):
            start = r*4+c
            print(currstate[start:start+1], end = "")
        print("\n", end="")
    print("\n")

def options ( currstate ):
    space = currstate.find(" ")
    possiblities = []
    
    for x in moves[space]:
        if space<x:
            possiblities.append( currstate[0:space] + currstate[x] + currstate[space+1:x] + currstate[space] + currstate[x+1:])
        else:
            possiblities.append( currstate[0:x] + currstate[space] + currstate[x+1:space] + currstate[x] + currstate[space+1:])
    # if space%3!=2: #Right
    #     possiblities.append( currstate[0:space] + currstate[space+1] + currstate[space] + currstate[space+2:]) 
    # if space%3!=0: #Left
    #     possiblities.append( currstate[0:space-1] + currstate[space] + currstate[space-1] + currstate[space+1:])
    # if space<6: #Down
    #     possiblities.append( currstate[0:space] + currstate[space+3] + currstate[space+1:space+3] + currstate[space] + currstate[space+4:])
    # if space>2: #Up
    #     possiblities.append( currstate[0:space-3] + currstate[space] + currstate[space-2:space] + currstate[space-3] + currstate[space+1:])    
    return possiblities
def printSolution(sol, dict):
    steps = []
    while sol!="":
        steps.insert(0, sol)
        sol = dict[sol]
    for s in steps[1:]:
        printstate(s)
    print("Steps: "+str(len(steps)-1))

def inversionCount(curr):
    curr=curr.replace(" ", "")
    return len([1 for i in range(len(curr)-1) for j in range(i+1, len(curr)) if int(curr[i], 16)>int(curr[j], 16)])
not_solved = True
goal = "123456789abcdef "
state = sys.argv[1].lower()
#state = '123456789abcdef '
rowSpacesaway = 3-state.find(" ")//4
state = state.translate({ord('_'): ' '})
printstate(state)
if (rowSpacesaway & 1)==(inversionCount(state)&1):
    toBeParsed = [state]
    alreadyParsed = {state:""}
    lowerbound = 0
    while(lowerbound<len(toBeParsed)):
        curr = toBeParsed[lowerbound]
        lowerbound+=1
        if(goal==curr):
            not_solved = False
            printSolution(curr, alreadyParsed)
            break   
        possibilities = options(curr)
        for x in possibilities:
            if not x in alreadyParsed:
                toBeParsed.append(x)
                alreadyParsed[x] = curr
else:
    print("No Solution to this puzzle")
