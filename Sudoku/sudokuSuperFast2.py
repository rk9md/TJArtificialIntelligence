import sys, time
rows = {}
columns = {}
boxes = {}
indexToConficts = {}
#puzzle = sys.argv[1]
#puzzle = "..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3.."
#initialSpaces = []
#size = int(len(puzzle)**.5+0.5)
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
    #if puzzle[x] == ".":
    #    initialSpaces.append(x)

indexToNeighbors = {y : set().union(rows[indexToConficts[y][0]], columns[indexToConficts[y][1]], boxes[indexToConficts[y][2]])-{y} for y in range(size**2)}
allSets = [boxes, rows, columns]
def pzlSymbols(pzl):
    return {z : symbols - {pzl[con] for con in indexToNeighbors[z]} for z in spaces}

# def returnDictVal(ind, dic):
#     return len(dic[ind])

# def orderSymbols(dic):
#     return sorted(dic, key=returnDictVal)
def best(pzl):
    index = 0
    options = {}
    mini = size+1
    tiny = set()
    for z in spaces:
        if pzl[z]==".":
            smallSet = symbols - {pzl[con] for con in indexToNeighbors[z]}
            options[z] = smallSet
            curr = len(smallSet)
            if curr==1:
                return (z, smallSet)
            if curr<mini:
                mini=curr
                tiny = smallSet
                index = z
    for y in boxes:
        nums = {x:set() for x in symbols}
        for b in boxes[y]:
            if pzl[b] == ".":
                for p in options[b]:
                    nums[p].add(b)



def isInvalid(pzl, index):
    conflict = indexToNeighbors[index]
    addition = pzl[index]
    for x in conflict:
        if addition == pzl[x]:
            return True
    return False

# def options():
#     return -1
def suduku(pzlTup):
    pzl = pzlTup[0]
    spaceChange = pzlTup[1]
    lastIndex = pzlTup[2]
    bestChoice = best(pzl)
    index = bestChoice[0]
    if spaceChange!=0 and isInvalid(pzl, lastIndex):  #1.33 seconds
        return ""
    if spaceChange== finish:  #0.0713 seconds
        return pzl
    for x in bestChoice[1]:
        result = suduku((pzl[:index]+x+pzl[index+1:], spaceChange+1, index))
        if result != "":          
            return result
    return ""

f = open("puzzles.txt", 'r')
toBeSolved = f.read().split("\n")

start = time.time()

count = 1
for puz in toBeSolved:
    spaces = []
    for x in range(81):
        if puz[x]==".":
            spaces.append(x)
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