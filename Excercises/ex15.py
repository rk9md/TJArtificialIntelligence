import sys
words = sys.argv[1].split(" ")
for x in range(0, len(words)):
    words[x] = words[x].upper()[0]+words[x][1:]
print(" ".join(words))