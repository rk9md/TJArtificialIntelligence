import sys
import time
import random
moves = {0:[1, 3], 1:[0, 2, 4], 2:[1, 5], 3:[0, 4, 6], 4:[1, 3, 5, 7], 5:[2, 4, 8], 6:[3, 7], 7:[4, 6, 8], 8:[5, 7]}
def printstate ( currstate ):
    for r in range(3):
        for c in range(3):
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
    return possiblities

def numberOfSteps(sol, dict):
    steps = []
    while sol!="":
        steps.insert(0, sol)
        sol = dict[sol]
    return len(steps)-1

def setOfSteps(sol, dict):
    steps = []
    while sol!="":
        steps.insert(0, sol)
        sol = dict[sol]
    return len(steps)

def solverv2(state, stateNotToBeIn):
    goal = "12345678 "
    state = state.translate({ord('_'): ' '})
    toBeParsed = [state]
    alreadyParsed = {state:""}
    while(len(toBeParsed)!=0):
        curr = toBeParsed.pop(0)
        if(goal==curr):
            return stateNotToBeIn not in setOfSteps(curr, alreadyParsed) 
        possibilities = options(curr)
        for x in possibilities:
            if not x in alreadyParsed:
                toBeParsed.append(x)
                alreadyParsed[x] = curr
    return False

def solver(state):
    not_solved = True
    goal = "12345678 "
    state = state.translate({ord('_'): ' '})
    toBeParsed = [state]
    alreadyParsed = {state:""}
    while(len(toBeParsed)!=0):
        curr = toBeParsed.pop(0)
        if(goal==curr):
            not_solved = False
            return numberOfSteps(curr, alreadyParsed) 
        possibilities = options(curr)
        for x in possibilities:
            if not x in alreadyParsed:
                toBeParsed.append(x)
                alreadyParsed[x] = curr
    return -1

def randomState():
    digits = ["1", "2", "3", "4", "5", "6", "7", "8", "_"]
    random.shuffle(digits)
    s = "".join(digits)   
    return s   

#def contraintC(state, dict, step):
    
    


def stepsTo(goal):
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
    maxSteps = move-2
    return chart

start = time.time()
solver("123456_87")
print("Time to determine if a puzzle is unsolvable: "+str(time.time() - start) + " seconds")

totalTime = 0
totalSteps = 0
viableStates = 0
   
for x in range(1000):
    start = time.time()
    steps = int(solver(randomState()))
    totalTime+=(time.time()-start)
    if(steps!=-1): #Negative One is the case solver gives if there is no solution
        totalSteps+=steps
        viableStates+=1
    
print("Average Time to Solve Puzzle: "+str(totalTime/1000)+" seconds")
print("Average Steps to Solve Puzzle: "+str(totalSteps/viableStates)+" steps")


stateSet = ["12345678 "]
distances = stepsTo("12345678 ")
for step in range(1,32):
    for state in distances[step]:
        if stateSet[-1] not in options(state):
            stateSet.append(state)
            break
print("Problem 8: "+str(stateSet))  
print(len(stateSet))

#8 Challenge
#stateSet = ["12345678 "]

# for step in range(1,32):
#     for state in distances[step]:
#         if stateSet[-1] not in options(state):
#             worked = True
#             for x in stateSet:
#                 if solverv2(state, x):
#                     worked = False
#             if worked:
#                 stateSet.append(state)
#                 break       
# print("Problem 8a: "+str(stateSet))  
# print(len(stateSet))