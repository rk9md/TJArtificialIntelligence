import sys
letters = {}
for y in sys.argv[1]:
    if y in letters:
        letters[y] = letters[y] + 1
    else:
        letters[y] = 1
maximum = 0
allMax = {}
for x in letters:
    if letters[x]>maximum:
        maximum = letters[x]
        letter = x
        allMax.clear()
        allMax[x] = maximum
    elif letters[x]==maximum:
        allMax[x] = maximum
for letter in allMax:
    print(letter + ": "+str(maximum)+" times")