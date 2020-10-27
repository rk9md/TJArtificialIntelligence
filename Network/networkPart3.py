import random
numOfNodes = 100000
avgDegree = 4
starter = int((avgDegree*2.5)//1)

nodes = {x:set() for x in range(starter)}
totalNumOfEdges = avgDegree*numOfNodes//2
weightList = [*range(starter)]
currEdges = 0

for x in range(avgDegree*starter):
    here = random.choice(range(starter))
    there = random.choice(weightList)
    while here==there or there in nodes[here]:
        here = random.choice(range(starter))
        there = random.choice(weightList)
    nodes[here].add(there)
    nodes[there].add(here)
    currEdges+=1

while starter<numOfNodes:
    nodes[starter] = set()
    currDegree = random.randint(1,avgDegree//2)
    here = starter
    for x in range(currDegree):
        there = random.choice(weightList)
        while here==there or there in nodes[here]:
            there = random.choice(weightList)
        nodes[here].add(there)
        nodes[there].add(here)
        currEdges+=1
    starter+=1

while currEdges<totalNumOfEdges:
    here = random.choice(range(starter))
    there = random.choice(weightList)
    while here==there or there in nodes[here]:
        here = random.choice(range(starter))
        there = random.choice(weightList)
    nodes[here].add(there)
    nodes[there].add(here)
    currEdges+=1

def listOfDegrees(nodes): #nodes is dictionary of node to set of connections
    return [len(nodes[x]) for x in nodes]
numOfEdgesPerNode = listOfDegrees(nodes)
totalNumOfEdgesAdded = sum(numOfEdgesPerNode)
def frequency(numOfEdgesPerNode):
    numOfEachDegree = {}
    for x in numOfEdgesPerNode:
        if x not in numOfEachDegree:
            numOfEachDegree[x] = 0
        numOfEachDegree[x]+=1
    return numOfEachDegree
def tuplifyAndSort(numOfEachDegree):
    return sorted([(x,numOfEachDegree[x]) for x in numOfEachDegree])
def printTuples(tuples):
    for x in tuples:
        print(x[0], x[1])
freq = frequency(numOfEdgesPerNode)
final = tuplifyAndSort(freq)
printTuples(final)
#print(totalNumOfEdgesAdded)

