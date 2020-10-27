hexagon = [{0,1,2,6,7,8}, {2,3,4,8,9,10}, {5, 6, 7, 12, 13, 14}, {7,8,9,14,15,16}, {9,10,11,16,17,18}, {13,14,15,19,20,21}, {15,16,17,21,22,23}]
diagonals = [{1,0,6,5,12}, {3,2,8,7,14,13,19}, {4,10,9,16,15,21,20}, {11,18,17,23,22}, {5,12,13,19,20}, {0,6,7,14,15,21,22}, {1,2,8,9,16,17,23}, {3,4,10,11,18}, {0,1,2,3,4}, {5,6,7,8,9,10,11}, {12,13,14,15,16,17,18}, {19,20,21,22,23}]
indexToHex = {}
indexToDiagonal = {}
for x in range(24):
    inThis =set()
    for y in range(len(hexagon)):
        if x in hexagon[y]:
            inThis.add(y)
    indexToHex[x] = inThis
for x in range(24):
    inThis =set()
    for y in range(len(diagonals)):
        if x in diagonals[y]:
            inThis.add(y)
    indexToDiagonal[x] = inThis

def checkRepeats(pzl, indecies):
    nums = set()
    for x in indecies:
        if pzl[x] !=".":
            if pzl[x] in nums:
                return True
            nums.add(pzl[x])
    return False
    #add all numbers to a set, while going through see if its already in the list
def isInvalid(pzl):
    invalid = False
    for x in hexagon:
        invalid = invalid or checkRepeats(pzl, x)
    return invalid
def isSolved(pzl):
    return "." not in pzl
def options(pzl, index):
    within = []
    for x in indexToHex[index]:
        within.append(set())
        size = len(within)-1
        for y in hexagon[x]:
            if not pzl[y]==".":
                within[size].add(pzl[y])
    finalOpt = {"A", "B", "C", "D", "E", "F"}
    for z in within:
        finalOpt = finalOpt.difference(z)
    return finalOpt

def bruteForce(pzlTup):
    pzl = pzlTup[0]
    curr = pzlTup[1]
    count1 = pzlTup[2]
    count2 = pzlTup[3]
    nex = curr+1
    if isInvalid(pzl) or count1>5 or count2>5:
        return ""
    if isSolved(pzl):
        if count1==5 and count2==5:
            return pzl
        else:
            return ""
    for poss in options(pzl, curr):
        newPzl = pzl[0:curr]+poss+pzl[curr+1:24]
        if poss == "A":
            result = bruteForce((newPzl, nex, count1+1, count2))
        elif poss == "B":
            result = bruteForce((newPzl, nex, count1, count2+1))
        else:
            result = bruteForce((newPzl, nex, count1, count2))
        
        if len(result)!=0:
            return result
    return ""
#start = "ABC...DEF..............."
start =  "........................"
print(len(start))

answer = bruteForce((start, 0, 0,0))
first = answer[0]
answer.replace(answer[0], "*")
answer.replace("A", first)
answer.replace("*", "A")
#answer = bruteForce((start, 0, 1, 1))
if answer!="":
    print(" "+answer[0:5])
    print(answer[5:12])
    print(answer[12:19])
    print(" "+answer[19:24])


# def isInvalidDiag(pzl):
#     invalid = False
#     for x in hexagon:
#         invalid = invalid or checkRepeats(pzl, x)
#     for y in diagonals:
#         invalid = invalid or checkRepeats(pzl, y)
#     return invalid
# def optionsDiag(pzl, index):
#     within = []
#     for x in indexToHex[index]:
#         within.append(set())
#         size = len(within)-1
#         for y in hexagon[x]:
#             if not pzl[y]==".":
#                 within[size].add(int(pzl[y]))
#     for x in indexToDiagonal[index]:
#         within.append(set())
#         size = len(within)-1
#         for y in diagonals[x]:
#             if not pzl[y]==".":
#                 within[size].add(int(pzl[y]))
#     finalOpt = {1,2, 3, 4, 5, 6, 7}
#     for z in within:
#         finalOpt = finalOpt.difference(z)
#     return finalOpt

# def bruteForceDiag(pzlTup):
#     pzl = pzlTup[0]
#     curr = pzlTup[1]
#     nex = curr+1
#     if isInvalidDiag(pzl):
#         return ""
#     if isSolved(pzl):
#         return pzl
#     for poss in optionsDiag(pzl, curr):
#         newPzl = pzl[0:curr]+str(poss)+pzl[curr+1:24]
#         result = bruteForceDiag((newPzl, nex))
#         if len(result)!=0:
#             return result
#     return ""

# print("\n\n\n")
# answer = bruteForceDiag((start, 0))
# if answer!="":
#     print(" "+answer[0:5])
#     print(answer[5:12])
#     print(answer[12:19])
#     print(" "+answer[19:24])    
# else:
#     print("No solution")