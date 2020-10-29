import sys, re, time
#Board input is in the format of characters and if a tile has multiple letters its like 2qu so a number that descibes its length. 
# maximum multiletter input is 4 letters
# boards must have n^2 number of tiles where n is greater than or equal to 4. 

#Starts the timer
start = time.time()

#Reads in the board and makes the string lowercase
board = sys.argv[1].lower()

#Array representation of the board
matrix = []

###############################################################
#Implement a board reading function for the multiletter tiles

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

# Number of tiles on the board
size  = len(matrix)

# Number of rows/cols in the board
n = int(size**0.5)

#The minimum length of an accepted word. If the board is 4x4, then minimum length for a valid word is 3, otherwise it will be 4.
minWord = (3 if n==4 else 4)


#For normal texts like wordsss
#Captures all words with a length of two or greater with either atleast one vowel or where w acts like a vowel (words with no other vowels) 
with open("scrabble.txt", mode='r') as f: scrabbleWords = {x.lower() for x in f.read().split() if re.search(r'^(((?=\w*[aeiouy])(a|[a-z]{2,}))|(?=\w*w)(?!\w*[aeiouy])([a-z]{2,}))$', x.lower())}


#lenWords = [{z for z in scrabbleWords if len(z)==x} for x in range(minWord,size)] # Divide the words into lengths
# Add the prefixes of all the words in scrabbleWords. Prefixes are parts of the word.
# For example, the word eaten has the prefixes e,ea,eat,eate
prefixes = {i:set() for i in range(size*4)}  # The reason the size of the prefixes is size*4 is cuz of the multiletter case otherwise the max word length is just size
for x in scrabbleWords:
    for s in range(1,len(x)):
        prefixes[s].add(x[:s])

coordinates = {x:(x//n, x%n) for x in range(size)} #PRECOMPUTE Coordinates for each index of matrix

# Given a coodinate tuple, return the index
def coordinateToIndex(coord):
    row = coord[0]
    col = coord[1]
    index = row*n+col
    return index

# Calculate the new coordinate based on the change given
def coordinateChange(orig, change):
    new = (orig[0]+change[0], orig[1]+change[1])
    return new

# Directions to move in, N, NW, W, SW, S, SE, E, NE
directions = [(0,1),(1,0),(0,-1),(-1,0),(1,1),(1,-1),(-1,-1),(-1,1)]

# Precompute each tile set of neighbors for each index of matrix
# For every valid direction from a tile, add the index of the neighboring tile to the set
neighbors = [] 
for x in range(size): 
    coor = coordinates[x]
    neighSet = set()
    for chan in directions:
        newCoord = coordinateChange(coor, chan) #change in the direction
        if newCoord[0]<n and newCoord[0]>=0 and newCoord[1]<n and newCoord[1]>=0: #If its within the board
            neighSet.add(coordinateToIndex(newCoord))
    neighbors.append(neighSet)
# This is the neighbors case of the start, you can start anywhere.
neighbors.append({*range(size)})
# The set of words found in the boggle puzzle
finalWords = set()
#word is the current word, tile is the index of the current tile in the linear array (enter the value size when there is no current position),
#visited is a set of tiles already visited
def recurForWords(word, tile, visited): 
    # Check if I have made a word only if the word length is higher than the minimum word length
    if len(word)>=minWord: 
        if word in scrabbleWords:
            finalWords.add(word)
    
    #Only continue building the current word if it is a prefix to another word or the empty string.
    #Recur on every possible neighboring tile that I have no already visited
    if word in prefixes[len(word)] or word=="": 
        neigh = neighbors[tile]
        for f in neigh:
            if f not in visited:
                try:
                    recurForWords(word+matrix[f], f, {*visited, f})
                except:
                    #Filler code
                    v=9-2

    else:
        return
# Start recursion with an empty word and any start position.
recurForWords("", size, set())

print(len(finalWords))

# print((time.time()-start))



