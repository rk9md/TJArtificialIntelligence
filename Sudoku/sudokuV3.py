import sys, time
rows = {}
columns = {}
boxes = {}
indexToConficts = {}
size = 9
possSymbols = "123456789abcdef0ghijklmnopqrstuvwxyz"
symbols = set(possSymbols[0:size])
for x in range(size**2):
    row = x//9
    column = x%9
    box = row//3*3+column//3
    conflicts = (row, column, box)
    if row not in rows:
        rows[row] = set()
    rows[row].add(x)
    if column not in columns:
        columns[column] = set()
    columns[column].add(x)
    if box not in boxes:
        boxes[box] = set()
    boxes[box].add(x)
    indexToConficts[x] = conflicts
constraintSets = [rows[x] for x in rows] +[columns[x] for x in columns]+[boxes[x] for x in boxes]
indexToNeighbors = {y : set().union(rows[indexToConficts[y][0]], columns[indexToConficts[y][1]], boxes[indexToConficts[y][2]])-{y} for y in range(size**2)}

def pzlSymbols(pzl):
    return {z : symbols - {pzl[con] for con in indexToNeighbors[z]} for z in spaces}

def best(pzl):
    # index = 0
    # mini = size+1
    # tiny = set()
    poss={}
    for z in range(81):
        if pzl[z]==".":
            smallSet = symbols - {pzl[con] for con in indexToNeighbors[z]}
            curr = len(smallSet)
            if curr == 0:
                return (False,set())
            if curr==1:
                return (smallSet.pop(), {z})
            # if curr<mini:
            #     mini=curr
            #     tiny = smallSet
            #     index = z
            poss[z] = smallSet
        else:
            poss[z] = {pzl[z]}
    minSym = 10
    lowSym = ""
    minSet = set()
    for checking in constraintSets:
        symbolDict = {x:set() for x in symbols}
        for ind in checking:
            if pzl[ind]==".":
                for sym in poss[ind]:
                    symbolDict[sym].add(ind)
        
        for x in symbolDict:
            curr = len(symbolDict[x])
            if curr==1:
                return (x, symbolDict[x])
            if minSym>curr and curr!=0:
                minSym=curr
                lowSym = x
                minSet = symbolDict[x]

    return (lowSym, minSet)

#def makeDeductions(pzl):
    

def isInvalid(pzl, index):
    conflict = indexToNeighbors[index]
    addition = pzl[index]
    for x in conflict:
        if addition == pzl[x]:
            return True
    return False


def suduku(pzlTup):
    pzl = pzlTup[0]
    spaceChange = pzlTup[1]

    bestChoice = best(pzl)
    index = bestChoice[1]
    symbol = bestChoice[0]
    # if index == False:
    #     return ""
    # while len(index)==1:#and spaceChange!= finish:
    #     ind = bestChoice[1].pop()
    #     #print(sym)
    #     pzl = pzl[:ind]+symbol+pzl[ind+1:]
    #     bestChoice = best(pzl)
    #     index = bestChoice[1]
    #     symbol = bestChoice[0]
    #     spaceChange+=1
    
    # if spaceChange!=0 and isInvalid(pzl, lastIndex):  #1.33 seconds
    #     return ""
    if spaceChange== finish:  #0.0713 seconds
        return pzl
    for x in index:
        result = suduku((pzl[:x]+symbol+pzl[x+1:], spaceChange+1))
        if result != "":          
            return result
    return ""

f = open("puzzles.txt", 'r')
toBeSolved = f.read().split("\n")

start = time.time()

count = 1
for puz in toBeSolved:
    spaces = set()
    for x in range(81):
        if puz[x]==".":
            spaces.add(x)
    #indexToNumbers = {i : {puz[x] for x in indexToNeighbors[i]}-{"."} for i in range(size**2)}
    # option = pzlSymbols(puz)
    # order = orderSymbols(option)
    # while len(order)!=0 and len(option[order[0]])==1:
    #     for x in range(len(order)):
    #         if len(option[order[x]])!=1:
    #             break
    #         puz = puz[:order[x]]+option[order[x]].pop()+puz[order[x]+1:]
    #         spaces.remove(order[x])
    #     option = pzlSymbols(puz)
    #     order = orderSymbols(option)
    finish = len(spaces)
    final = suduku((puz, 0, -1))
    
    print(str(count)+": "+final)
    count+=1
print(str(time.time()-start)+" seconds")