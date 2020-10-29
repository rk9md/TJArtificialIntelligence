import sys
import time
#build a graph of sixletter words where the vertexes are words and edges are between words that differ by exactly one letter

#Start the timer
first = time.time()

#Read in the words file to build the vertices.
f = open("words.txt", mode='r')
s = set(f.read().split("\n"))
s.remove("")
# A dictionary that maps a vertex to its edges
words={}
for x in s:
    words[x] = set()

# Number of edges
edges = 0
# Maximum number of neighbors
maxNeigh = 0
# List of words with the maximum number of neighbors
maxWords=[]

# For every two words, if they differ by exactly 1 one letter, connect them with an edge
for v in s:
    for v2 in s:
        count = 0
        for x in range(0, 6):
            if v[x]!=v2[x]:
                count+=1
        if(count==1):
            edges+=1
            words[v].add(v2)
            words[v2].add(v)

#The amount of time taken to build the graph             
part1 = time.time()-first

print("Number of Verticies: "+str(len(s)))
print("Number of Edges: "+str(edges//2))

# Find the words with the greatest number of neighbors
for w in words:
    if maxNeigh<len(words[w]):
        maxWords.clear()
        maxWords.append(w)
        maxNeigh = len(words[w])
    elif maxNeigh==len(words[w]):
         maxWords.append(w)         


#Find the number of connected components in the graph and the size of the largest one.

connectedcomp = 0
conMax = 0

# The set of verticies the algorithm has already been to
seen = set()
# The set of verticies the algorithm can choose to visit next
looking = set()

#While the number of words unvisited is not zero, pop a starting point for a component and begin building it.
while len(s)!=0:
    connectedcomp+=1
    start = s.pop()  
    seen.add(start)
    looking.add(start)
    # While the algorithm still has verticies to visit, pop one of them out and go through its neighbors. 
    # If the neighbor is not in seen (has not been visited yet), add it to seen and add its neighbors to looking.
    # Remove the neighbor from words in s. 
    while len(looking)!=0:
        curr = looking.pop()
        for x in words[curr]:
            if x not in seen:
                looking.add(x)
                seen.add(x)
                if x in s:
                    s.remove(x)
    # Once the while loop is done, you have visited all the verticies in this connected component.
    # The number of verticies in the connected component is the number of elements in seen.
    # Reset seen for the next component
    conMax = max(conMax, len(seen))
    seen.clear()
# If given a command line argument, print out the number of neighbors it has.
if len(sys.argv)>1:
    if sys.argv[1] in words:
        print(sys.argv[1] + " has the neighbors "+ ", ".join(sorted(words[sys.argv[1]])))

# Print the required statistics of the graph and the code.
print("The words with the most neighbors "+str(maxNeigh)+" are: " + ", ".join(maxWords))
print("Number of Connected Components: "+str(connectedcomp))
print("Largest Connected Component: "+str(conMax)+" Verticies")
print(str(part1) +" seconds taken to read and build my data structure")
print(str(time.time()-first) +" seconds taken to run")
