import sys, random, time
numOfNodes = 7
starter = 5 
nodes = {x:set() for x in range(starter)}
avgDegree = 4

totalNumOfEdges = avgDegree*numOfNodes*2
totalEdgesAdded = 0
weightList = [*range(starter)]

topNode = starter


while totalEdgesAdded<starter*4:
    here = random.choice(weightList)
    there = random.choice(weightList)
    if there not in nodes[here] and here!=there:
        nodes[here].add(there)
        nodes[there].add(here)
        totalEdgesAdded +=2
        weightList.append(here)
        weightList.append(there)

while topNode<numOfNodes:
    nodes[topNode] = set()
    numOfEdges = random.randint(0,avgDegree-1)
    # if topNode == numOfNodes - 1:
    #     numOfEdges = totalNumOfEdges - totalEdgesAdded
    for y in range(numOfEdges):
        connection = random.choice(weightList)
        while connection in nodes[topNode] or topNode!=connection:
            connection = random.choice(weightList)
        nodes[topNode].add(connection)
        nodes[connection].add(topNode)
        totalEdgesAdded+=2
        weightList.append(topNode)
        weightList.append(connection)
    topNode+=1


numOfEachDegree = {}
#for x in range(totalNumOfEdgesAdded-totalNumOfEdges):

def listOfDegrees(nodes): #nodes is dictionary of node to set of connections
    return [len(nodes[x]) for x in nodes]
numOfEdgesPerNode = listOfDegrees(nodes)
totalNumOfEdgesAdded = sum(numOfEdgesPerNode)

# print(totalNumOfEdgesAdded, totalNumOfEdges//2,"before", len(nodes))
# while totalNumOfEdgesAdded<totalNumOfEdges//2:
#     print(weightList)
#     here = weightList[random.randint(0, len(weightList)-1)]
#     there = [*nodes[here]][random.randint(0, len(nodes[here])-1)]
#     if there not in nodes[here] and here!=there:
#         nodes[here].add(there)
#         nodes[there].add(here)
#         totalNumOfEdgesAdded +=2
#         weightList.append(here)
#         weightList.append(there)

# print(totalNumOfEdgesAdded, totalNumOfEdges//2,"before2", len(nodes))
# while totalNumOfEdgesAdded>totalNumOfEdges//2:
#     here = weightList[random.randint(0, len(weightList)-1)]
#     there = weightList[random.randint(0, len(weightList)-1)]
#     if here in nodes and there not in nodes[here] and here!=there:
#         nodes[here].remove(there)
#         nodes[there].remove(here)
#         totalNumOfEdgesAdded -=2
    
def frequency(numOfEdgesPerNode):
    numOfEachDegree = {}
    for x in numOfEdgesPerNode:
        if x not in numOfEachDegree:
            numOfEachDegree[x] = 0
        numOfEachDegree[x]+=1
def tuplifyAndSort(numOfEachDegree):
    return sorted([(x,numOfEachDegree[x]) for x in numOfEachDegree])

print(totalNumOfEdgesAdded)
#print(sorted(numOfEdgesPerNode))
