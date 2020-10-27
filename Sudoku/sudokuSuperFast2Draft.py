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

def pzlSymbols(pzl):
    return {z : [i for i in range(size**2) if checkValid(pzl, i, z)] for z in symbols}

def returnDictVal(ind):
    return len(option[ind])

def orderSymbols(dic):
    return sorted(dic, key=returnDictVal)

def checkValid(pzl, index, symbol):
    conflict = indexToNeighbors[index]
    addition = symbol
    for x in conflict:
        if addition == pzl[x]:
            return False
    return True

def isInvalid(pzl, index):
    if pzl[index] != ".":
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
    symbol = pzlTup[1]
    lastChange = pzlTup[2]
    if isInvalid(pzl, lastChange):  #1.33 seconds
        return ""
    if lastChange == option[order[-1]][-1]:  #0.0713 seconds
        return pzl
    
    for x in option[symbol]:
        result = suduku((pzl[:index]+x+pzl[index+1:], spaceChange+1))
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
    
    option = pzlSymbols(puz)
    order = orderSymbols(option)
    for x in range(len(order)):
        if len(option[order[x]])!=1:
            break
        puz = puz[:order[x]]+option[order[x]].pop()+puz[order[x]+1:]
    option = pzlSymbols(puz)
    order = orderSymbols(option)
    finish = len(order)
    final = suduku((puz, 0))
    
    print(str(count)+": "+final)
    count+=1
print(str(time.time()-start)+" seconds")