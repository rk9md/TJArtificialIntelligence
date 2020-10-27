import sys
import time
first = time.time()
letters = "abcdefghijklmnopqrstuvwxyz"
f = open("words.txt", mode='r')
s = set(f.read().split("\n"))
s.remove("")
words={}
print("Number of Verticies: "+str(len(s)))
edges = 0
maxNeigh = 0
maxWords=[]
for v in s:
    perm = set()
    for x in v:
        part = v.replace(x, "*")
        for alpha in letters:
            perm.add(part.replace("*", alpha))
    perm.remove(v)
    perm.intersection_update(s)
    words[v] = perm
    length = len(perm)
    edges+=length
    if maxNeigh<length:
        maxWords.clear()
        maxWords.append(v)
        maxNeigh = length
    elif maxNeigh==length:
         maxWords.append(v)
part1 = time.time()-first
print("Number of Edges: "+str(edges//2))

             



seen = set()
looking = set()
connectedcomp = 0
conMax = 0
while len(s)!=0:
    connectedcomp+=1
    start = s.pop()  
    seen.add(start)
    looking.add(start)
    while len(looking)!=0:
        curr = looking.pop()
        for x in words[curr]:
            if x not in seen:
                looking.add(x)
                seen.add(x)
                if x in s:
                    s.remove(x)
    conMax = max(conMax, len(seen))
    seen.clear()
if len(sys.argv)>1:
    if sys.argv[1] in words:
        print(sys.argv[1] + " has the neighbors "+ ", ".join(words[sys.argv[1]]))
print("The words with the longest length of "+str(maxNeigh)+" are: " + ", ".join(maxWords))
print("Number of Connected Components: "+str(connectedcomp))
print("Largest Connected Component: "+str(conMax)+" Verticies")
print(str(part1) +" seconds taken to read and build my data structure")
print(str(time.time()-first) +" seconds taken to run")
