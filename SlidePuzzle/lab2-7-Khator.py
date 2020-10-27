import sys
moves = {0:[1, 3], 1:[0, 2, 4], 2:[1, 5], 3:[0, 4, 6], 4:[1, 3, 5, 7], 5:[2, 4, 8], 6:[3, 7], 7:[4, 6, 8], 8:[5, 7]}
def printstate ( currstate ):
    for r in range (3):
        for c in range (3):
            start = r*3+c
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

def solver(state):
    not_solved = True
    goal = "12345678 "
    state = state.translate({ord('_'): ' '})
    printstate(state)
    toBeParsed = [state]
    alreadyParsed = {state:""}
    while(len(toBeParsed)!=0):
        curr = toBeParsed.pop(0)
        if(goal==curr):
            not_solved = False
            printSolution(curr, alreadyParsed)   
        possibilities = options(curr)
        for x in possibilities:
            if not x in alreadyParsed:
                toBeParsed.append(x)
                alreadyParsed[x] = curr
    if not_solved:
        print("No Solution to this puzzle")

#Expression = 9!
goal = "12345678 "
move = 1
toBeParsed = [goal]
nextLevel = []
alreadyParsed = {goal}
chart = {0:{goal}}

while(len(toBeParsed)!=0):
    curr = toBeParsed.pop(0)  
    possibilities = options(curr)
    for x in possibilities:
        if x not in alreadyParsed:
            nextLevel.append(x)
            alreadyParsed.add(x)
            if move in chart:
                chart[move].add(x)
            else:
                chart[move] = {x}
    if len(toBeParsed)==0:
        move+=1
        toBeParsed+=nextLevel
        nextLevel.clear()
maxSteps = move-2 #Just an adjustment made to move to account for the while loop over counting. Always two over.
for x in range(int((maxSteps+1)/2)):
    print(str(x)+":"+str(len(chart[x]))+"\t\t"+str(x+16)+":"+str(len(chart[x+16])))
print("")
solver(chart[maxSteps].pop())