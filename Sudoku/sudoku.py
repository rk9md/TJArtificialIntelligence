import sys, time
rows = {}
columns = {}
boxes = {}
indexToConficts = {}

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

def suduku(pzlTup):
    pzl = pzlTup[0]
    lastChange = pzlTup[1]
    index = pzl.find(".")
    if isInvalid(pzl, lastChange):
        return ""
    if index == -1:
        return pzl
    for x in symbols:
        result = suduku((pzl[:index]+x+pzl[index+1:], index))
        if result != "":
            return result
    return ""

f = open("puzzles.txt", 'r')
toBeSolved = f.read().split("\n")


start = time.time()
count = 1
for puz in toBeSolved[0:51]:
    final = suduku((puz, 0))
    print(str(count)+": "+final)
    count+=1
print(str(time.time()-start)+" seconds")