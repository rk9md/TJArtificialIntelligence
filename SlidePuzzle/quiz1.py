import sys
import time
import random
moves = {0:[1, 3], 1:[0, 2, 4], 2:[1, 5], 3:[0, 4, 6], 4:[1, 3, 5, 7], 5:[2, 4, 8], 6:[3, 7], 7:[4, 6, 8], 8:[5, 7]}
def options ( currstate ):
    space = currstate.find(" ")
    possiblities = []
    for x in moves[space]:
        if space<x:
            possiblities.append( currstate[0:space] + currstate[x] + currstate[space+1:x] + currstate[space] + currstate[x+1:])
        else:
            possiblities.append( currstate[0:x] + currstate[space] + currstate[x+1:space] + currstate[x] + currstate[space+1:])    
    for x in possiblities:
        if abs(inversionCount(currstate)-inversionCount(x))>4:
            possiblities.remove(x)

    return possiblities

def printSolution(sol, dict):
    steps = []
    while sol!="":
        steps.insert(0, sol)
        sol = dict[sol]
    for s in steps[1:]:
        printstate(s)
    print("Steps: "+str(len(steps)-1))
def printstate ( currstate ):
    for r in range (3):
        for c in range (3):
            start = r*3+c
            print(currstate[start:start+1], end = "")
        print("\n", end="")
    print("\n")
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
            return printSolution(curr, alreadyParsed)   
        possibilities = options(curr)
        for x in possibilities:
            if not x in alreadyParsed:
                toBeParsed.append(x)
                alreadyParsed[x] = curr
    if not_solved:
        print("No Solution to this puzzle")

def checker1(state):
    for plop in range(len(state)):
        x = state[plop]
        if not x==" ":
            num = int(x)
            for y in moves[plop]:
                zop = state[y]
                if not zop==" ":
                    zop = int(zop)
                    if(abs(num-zop)==1):
                        return True
def checker2(state, start):
    for x in range(len(start)):
        if state[x]==start[x]:
            return False
    return True

def inversionCount(curr):
    curr=curr.replace(" ", "")
    return len([1 for i in range(len(curr)-1) for j in range(i+1, len(curr)) if int(curr[i], 16)>int(curr[j], 16)])

def checker3(state):
    steps = solver(state)
    steps.insert(0, state)
    for x in range(len(steps)-1):
        if abs(inversionCount(steps[x])-inversionCount(steps[x+1]))>4:
            return False

def neigh(goal):
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
                # if checker1(x):
                #     return x
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
    maxSteps = move-2
    return chart

def shortestposDif(goal):
    move = 1
    toBeParsed = [goal]
    nextLevel = []
    alreadyParsed = {goal}
    while(len(toBeParsed)!=0):
        curr = toBeParsed.pop(0)
        possibilities = options(curr)
        for x in possibilities:
            if x not in alreadyParsed:
                if checker2(x, goal):
                    return (x, move)
                nextLevel.append(x)
                alreadyParsed.add(x)
        if len(toBeParsed)==0:
            move+=1
            toBeParsed+=nextLevel
            nextLevel.clear()
    maxSteps = move-2

def posDif(goal):
    move = 1
    toBeParsed = [goal]
    nextLevel = []
    alreadyParsed = {goal}
    chart = {}
    while(len(toBeParsed)!=0):
        #chart[move] = set()
        curr = toBeParsed.pop(0)
        possibilities = options(curr)
        for x in possibilities:
            if x not in alreadyParsed:
                if checker2(x, goal):
                    chart[move] = x
                nextLevel.append(x)
                alreadyParsed.add(x)
        if len(toBeParsed)==0:
            move+=1
            toBeParsed+=nextLevel
            nextLevel.clear()
    maxSteps = move-2
    return chart

state = "17283564 "
spaces = {"12345678 ", "1234567 8", "123456 78", "12345 678", "1234 5678", "123 45678", "12 345678", "1 2345678", " 12345678"}
for x in spaces:
    print(x)
    z = neigh(x)
    zmax = max(z)
    print(str(zmax) + " " +str(z[zmax]))

#solver("8672543 1")
#print(checker2("12345678 ", "412583 76"))
