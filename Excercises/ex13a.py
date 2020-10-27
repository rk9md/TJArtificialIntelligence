import sys
letters = {}
for x in sys.argv[1]:
    if x in letters:
        letters[x] = letters[x] + 1
    else:
        letters[x] = 1
maximum = 0
letter = ""
for x in letters:
    if letters[x]>maximum:
        maximum = letters[x]
        letter = x
print(letter + ": "+str(maximum)+" times")