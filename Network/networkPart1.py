import sys, random, time
numOfNodes = 100000
nodes = {x:set() for x in range(numOfNodes)}
avgDegree = 5
totalNumOfEdges = avgDegree*numOfNodes*2
totalEdgesAdded = 0


##########################################################
nodeList = [*range(numOfNodes)]
totalEdgesAdded = 0
while totalEdgesAdded<totalNumOfEdges//2:
    here = random.randint(0, numOfNodes-1)
    there = random.randint(0, numOfNodes-1)
    if there not in nodes[here] and here!=there:
        nodes[here].add(there)
        nodes[there].add(here)
        totalEdgesAdded +=2
numOfEdgesPerNode = [len(nodes[x]) for x in nodes]
totalNumOfEdgesAdded = sum(numOfEdgesPerNode)
numOfEachDegree = {}

for x in numOfEdgesPerNode:
    if x not in numOfEachDegree:
        numOfEachDegree[x] = 0
    numOfEachDegree[x]+=1

print(sorted([(x,numOfEachDegree[x]) for x in numOfEachDegree]))
print(totalNumOfEdgesAdded)

