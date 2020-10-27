import sys, time, random
spaceMoves = {0:[(0,1,3), (0, 2, 5)], 1:[(1, 3, 6), (1, 4, 8)], 2:[(2, 4, 7), (2, 5, 9)], 3:[(3, 6, 10),(3, 7, 12), (3,4,5), (3,1,0)], 4:[(4, 7, 11), (4, 8, 13)], 5:[(5,8,12),(5,9,14),(5,4,3), (5, 2, 0)], 6:[(6, 7, 8), (6, 3,1)], 7:[(7, 8, 9), (7, 4, 2)], 8:[(8, 7, 6), (8, 4, 1)], 9:[(9,8,7),(9,5,2)], 10:[(10, 11, 12),(10, 6, 3)], 11:[(11, 12, 13),(11, 7, 4)], 12:[(12, 11, 10),(12, 7, 3), (12, 8, 5), (12, 13, 14)], 13:[(13, 12, 11), (13,8,4)], 14:[(14, 13, 12), (14, 9, 5)]}
hexa = {"0":0, "1":1, '2':2, '3':3, '4':4, '5':5, '6':6 ,'7':7 ,'8':8, '9':9, "a":10, 'b':11, "c":12, 'd':13, 'e':14}
backHexa = {}
for x in hexa:
    backHexa[hexa[x]]= x
def isPuzzleAtGoal(state):
    return len(state.translate({ord(' '): ''}))==1
def nbrFromPzl(pzl,fromPos, overPos, toPos, spaces):
    spacePoses = []
    for x in spaces:
        spacePoses.append(x)
    if fromPos<toPos:
        newPzl = pzl[0:fromPos]+" "+pzl[fromPos+1:overPos]+" "+pzl[overPos+1:toPos]+backHexa[toPos]+pzl[toPos+1:]
    else:
        newPzl = pzl[0:toPos]+backHexa[toPos]+pzl[toPos+1:overPos]+" "+pzl[overPos+1:fromPos]+" "+pzl[fromPos+1:]
    spacePoses.append(fromPos)
    spacePoses.append(overPos)
    spacePoses.remove(toPos)
    return (newPzl, fromPos, toPos, spacePoses)
def nbrsFromPzl(pzlTup):
    pzl = pzlTup[0]
    spaces = pzlTup[3]
    neighbors = []
    for x in spaces:
        for trips in spaceMoves[x]:
            tPos = trips[0]
            oPos = trips[1]
            fPos = trips[2]
            if pzl[oPos]!=" " and pzl[fPos]!=" ":# and pzl[tPos]==" ":
                neighbors.append(nbrFromPzl(pzl, fPos, oPos, tPos, spaces))
    return neighbors

def printSolution(sol, dict):
    steps = []
    while sol!="":
        tup = dict[sol]
        sol = tup[0]
        #steps.append(sol)
        if tup[1]==13 and tup[2]==4:
            print(sol)
        steps.append((tup[1], tup[2]))
    for s in steps[::-1]:
        if s != (0, 0):
        #if s == "":

            print(str(s[0])+" --> "+str(s[1]))
            #printer(s)

def printer(arr):
    print("                ", arr[0], "        ")
    print("            ", arr[1], "    ", arr[2], "        ")
    print("      ", arr[3], "      ",arr[4], "      ",arr[5], "        ")
    print("  ", arr[6], "      ",arr[7], "     ",arr[8], "    ", arr[9], "     ")
    print("", arr[10], "     ",arr[11], "     ",arr[12], "     ", arr[13], "     ", arr[14], "        ")
    print()

spaceIndex = sys.argv[1]
#spaceIndex = "4"
orignal = "0123456789abcde"
state = (orignal.replace(spaceIndex, " "), 0, 0, [int(spaceIndex)])
toBeParsed = [state]
alreadyParsed = {state[0]:("", 0, 0)}
lowerbound = 0
while(lowerbound<len(toBeParsed)):
    curr = toBeParsed[lowerbound]
    currpzl = curr[0]
    #print(currpzl)
    lowerbound+=1
    if isPuzzleAtGoal(currpzl):
        printSolution(currpzl, alreadyParsed)
        break
    possibilities = nbrsFromPzl(curr)
    for x in possibilities:
        nextPzl = x[0]
        if not nextPzl in alreadyParsed:
            toBeParsed.append(x)
            alreadyParsed[nextPzl] = (currpzl, x[1], x[2])