import sys, re, time
start = time.time()
board = sys.argv[1].lower()
matrix = []

###############################################################
#Implement a board reading funciotn for the multiletter stuff #

count = 0
while count<len(board):
    if board[count].isdigit():
        letter = board[count+1:count+int(board[count])+1] #if a tile has multiple letters in it
        count+=int(board[count])
    else:
        letter =  board[count]
    count+=1
    matrix.append(letter)
###############################################################
size  = len(matrix)
n = int(size**0.5)
minWord = (3 if n==4 else 4)


#For normal texts like wordsss
with open("scrabble.txt", mode='r') as f: scrabbleWords = {x.lower() for x in f.read().split() if re.search(r'^(((?=\w*[aeiouy])(a|[a-z]{2,}))|(?=\w*w)(?!\w*[aeiouy])([a-z]{2,}))$', x.lower())}

# f = open("scrabble.txt", mode='r')
# scrabbleWords = {x.lower() for x in f.read().splitlines()}


#print(scrabbleWords)
#scrabbleWords = {x for x in f.read().splitlines() if x != ""}
#lenWords = [{z for z in scrabbleWords if len(z)==x} for x in range(minWord,size)]
prefixes = {i:set() for i in range(size*4)}  # The reason the size of the prefixes is size*4 is cuz of the multiletter case otherwise the max word length is just size
for x in scrabbleWords:
    for s in range(1,len(x)):
        prefixes[s].add(x[:s])


#lenPre = [{z for z in scrabbleWords if len(z)==x} for x in range(minWord,size*3)]
coordinates = {x:(x//n, x%n) for x in range(size)} #PRECOMPUTE coord changes
def coordinateToIndex(coord):
    row = coord[0]
    col = coord[1]
    index = row*n+col
    return index
def coordinateChange(orig, change):
    new = (orig[0]+change[0], orig[1]+change[1])
    return new
directions = [(0,1),(1,0),(0,-1),(-1,0),(1,1),(1,-1),(-1,-1),(-1,1)]
#neighbors = [{} for x in range(size)]
neighbors = [] #precompute each tile neighbors
for x in range(size): 
    coor = coordinates[x]
    neighSet = set()
    for chan in directions:
        newCoord = coordinateChange(coor, chan) #change in the direction
        #print(newCoord)
        if newCoord[0]<n and newCoord[0]>=0 and newCoord[1]<n and newCoord[1]>=0: #If its within the board
            neighSet.add(coordinateToIndex(newCoord))
    neighbors.append(neighSet)
neighbors.append({*range(size)})

finalWords = set()
def recurForWords(word, tile, visited): #word is the current word, tile is the index of the current tile in the linear array, visited is a set of tiles already visited
    #print(word)
    if len(word)>=minWord: #check if i have made a word only if the word lenght is higher than the minimum word length
        if word in scrabbleWords:
            finalWords.add(word)
            #print(word)
    if word in prefixes[len(word)] or word=="": #if valid prefix or  empty word
        neigh = neighbors[tile]
        for f in neigh:
            if f not in visited:
                try:
                    recurForWords(word+matrix[f], f, {*visited, f})
                except:
                    #print(f)
                    v=9-2

    else:
        return
recurForWords("", size, set())
#print(finalWords)
print(len(finalWords))

#print(matrix)
# print((time.time()-start))

# print(prefixes)


