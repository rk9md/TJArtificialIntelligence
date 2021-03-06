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
symbols = possSymbols[0:size]
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

def isInvalid(pzl, index):
    if pzl[index] != ".":
        conflict = indexToConficts[index]
        addition = pzl[index]
        for x in rows[conflict[0]]:
            if x!=index and addition == pzl[x]:
                return True
        for x in columns[conflict[1]]:
            if x!=index and addition == pzl[x]:
                return True
        for x in boxes[conflict[2]]:
            if x!=index and addition == pzl[x]:
                return True
    return False

# def options():
#     return -1

def suduku(pzlTup):
    pzl = pzlTup[0]
    spaceChange = pzlTup[1]
    if isInvalid(pzl, spaces[spaceChange-1]):
        return ""
    if spaces[spaceChange-1] == spaces[-1] and spaceChange!=0:
        return pzl
    index = spaces[spaceChange]
    for x in symbols:
        result = suduku((pzl[:index]+x+pzl[index+1:], spaceChange+1))
        if result != "":
            return result
    return ""

f = open("puzzles.txt", 'r')
toBeSolved = f.read().split("\n")

start = time.time()
count = 1
for puz in toBeSolved[0:51]:
    spaces = []
    for x in range(81):
        if puz[x]==".":
            spaces.append(x)
    final = suduku((puz, 0))
    print(str(count)+": "+final)
    count+=1
print(str(time.time()-start)+" seconds")