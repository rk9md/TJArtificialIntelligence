from tkinter import *
import math, time, sys
numberBeforeUpdate = 100
fringeColor = "blue" #Color of the Edge Nodes
visitedColor = "green" #Color of the nodes already visited
startColor = "red" #Color of the start node
endColor = "purple" #Color of the end node
USColor = "black" #Color of the US railroads
city1 = "Las Vegas" #Start City
city2 = "Atlanta" #End City


class Heap:
    
    def __init__(self):
        self.array = [(-1,"blank")]
        self.size = 0
        self.indecies = {}
    # def size(self):
    #     return self.size
    def swap(self, k, z):
        self.indecies[self.array[z][1]] = k
        self.indecies[self.array[k][1]] = z
        self.array[z], self.array[k]  = self.array[k], self.array[z]

    def inThis(self, state):
        return state in self.indecies

    def heapUp(self, k):
        while k>1 and self.array[k][0]<self.array[k//2][0]:
            self.swap(k, k//2)
            k = k//2
    def heapDown(self, k):
        while k*2+1<=self.size and (int(self.array[k][0])>int(self.array[k*2][0]) or int(self.array[k][0])>int(self.array[k*2+1][0])):
            if int(self.array[k*2][0])<int(self.array[k*2+1][0]):
                self.swap(k, k*2)
                k=k*2
            else:
                self.swap(k, k*2+1)
                k=k*2+1
        if k*2<=self.size and int(self.array[k*2][0])<int(self.array[k][0]):
            self.swap(k, k*2)
    def add(self, item):
        self.array.append(item)
        self.size+=1
        self.indecies[item[1]] = self.size 
        self.heapUp(self.size)
        
    def remove(self):
        self.swap(1, self.size)
        self.size-=1
        obj = self.array.pop()
        del self.indecies[obj[1]]
        self.heapDown(1)
        return obj

    def find(self, state):
        return self.indecies[state]
        # if self.inThis():
        #     for x in range(self.array):
        #         if self.array[x][1]==state:
        #             return x
    def update(self, state, newPriority, parent, cost):
        index = self.find(state)
        tup = self.array[index]
        self.array[index] = (newPriority, tup[1], cost, parent)

weight = 1
def heuristic(here, goal, cost):
    return (distance(nodesToCoordinates[here], nodesToCoordinates[goal]))*weight+cost



def toRadians(num):
    return num*math.pi/180
def distance(here, there):
    r = 6371 #km
    #r = 3959 #miles
    la1 = toRadians(here[0])
    la2 = toRadians(there[0])
    dLo = toRadians(there[1])- toRadians(here[1])
    dLa = la2-la1 
    a = math.sin(dLa/2)*math.sin(dLa/2) + math.cos(la1)*math.cos(la2) * math.sin(dLo/2)*math.sin(dLo/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    return r*c


prefix = "rr"

initial = time.time()
f = open(prefix+"Nodes.txt", mode='r')
citiesToID = {}
idToCities = {}
nodesToCoordinates = {}
rails = {}
lat = set()
longi = set()
nodes = f.read().split()
edgeToDistance = {}
#print(nodes)
x=0
while x<len(nodes):
    nodesToCoordinates[nodes[x]] = (float(nodes[x+1]), float(nodes[x+2]))  #(Lat, Long)
    lat.add(float(nodes[x+1]))
    longi.add(float(nodes[x+2]))
    x+=3
f.close()

e = open(prefix+"Edges.txt", mode='r')
edges = e.read().split()
edge = set(edges)
for x in range(0,len(edges),2):
    if edges[x] not in rails:
        rails[edges[x]] = set()
    rails[edges[x]].add(edges[x+1])
    if edges[x+1] not in rails:
        rails[edges[x+1]] = set()
    rails[edges[x+1]].add(edges[x])
    costToGo = distance(nodesToCoordinates[edges[x]], nodesToCoordinates[edges[x+1]])
    edgeToDistance[(edges[x+1], edges[x])] = costToGo
    edgeToDistance[(edges[x], edges[x+1])] = costToGo
e.close()


n = open("rrNodeCity.txt")
names = n.read().split("\n")
names.remove("")
for x in range(0, len(names)):
    line = names[x].split()
    number = line[0]
    ct = " ".join(line[1:])
    citiesToID[ct]=number
    idToCities[number] = ct
n.close()

master= Tk()
scale = 15
buffer = 30
maxLong = max(longi)
minLong = min(longi)
maxLat = max(lat)
minLat = min(lat)
mapWidth = (maxLong-minLong)*scale + buffer*2
mapLength = (maxLat-minLat)*scale + buffer*2

def coordinates(intial):
    latitude = intial[0]
    lon = intial[1]
    newLon = (lon-minLong)*scale+buffer
    newLat = (maxLat - latitude)*scale+buffer
    return (newLat, newLon)

#print(maxLong, minLong, maxLat, minLat)
c = Canvas(master, width=mapWidth, height=mapLength)
c.pack()

def makeLine(here, there):
    coorde = coordinates(nodesToCoordinates[here])
    othercoord = coordinates(nodesToCoordinates[there])
    c.create_line(coorde[1], coorde[0], othercoord[1], othercoord[0], fill="red", width=3)

alreadySeen = set()
parsing = {nodes[0]}
while len(parsing)!=0:
    curr = parsing.pop()
    coord = coordinates(nodesToCoordinates[curr])
    for x in rails[curr]:
        if x not in alreadySeen:
            # makeLine(curr, x)
            otherCoord = coordinates(nodesToCoordinates[x])
            c.create_line(coord[1], coord[0], otherCoord[1], otherCoord[0], fill = USColor)
            parsing.add(x)
    alreadySeen.add(curr)


#print(distance((50, -5), (58, -3)))
dist = 0
for x in edgeToDistance:
    dist+=edgeToDistance[x]
print("Total Distance is "+str(dist) + " kilometers")
#mainloop()

def showPath(goal, closed):
    first = goal
    path  = [first]
    costs = []
    dad = closed[first]
    #print("City Distance(km)")
    while dad!="":
        makeLine(first, dad)
        c.update()
        path.append(dad)
        costs.append(edgeToDistance[(first, dad)])
        first = dad
        dad = closed[first]
    costs = costs[::-1]
    path = path[::-1][1:]
    print(idToCities[first])
    sumD = 0
    for x in range(len(path)):
        sumD+=costs[x]
        if path[x] in idToCities:
            print(idToCities[path[x]], str(costs[x])+" km")
        else:
            print(path[x], str(costs[x])+" km")
    print("Shortest Distance: "+ str(sumD)+" km")
def create_circle(x, y, r, filler):
    c.create_oval(x-r, y-r, x+r, y+r, fill=filler)



for x in range(1, len(sys.argv)-1):
    #print(sys.argv[x])
    city1 = " ".join(sys.argv[1: x+1])
    city2 = " ".join(sys.argv[x+1:])
    if city1 in citiesToID:
        if city2 in citiesToID:
            break
start = citiesToID[city1]
goal = citiesToID[city2]
begin = coordinates(nodesToCoordinates[start])
create_circle(begin[1], begin[0], 10, startColor)
end = coordinates(nodesToCoordinates[goal])
create_circle(end[1], end[0], 10, endColor)
#print(start, goal)
closedSet = {}
openSet = Heap()
hMap = {}
h = heuristic(start,goal, 0)
hMap[start] = h 
openSet.add((h, start, 0, ""))
notFound = True
pops = 0
while openSet.size!=0 and notFound:
    curr = openSet.remove()
    pops+=1
    place = curr[1]
    heur = curr[0]
    cost = curr[2]
    parent = curr[3]
    green = coordinates(nodesToCoordinates[place])
    create_circle(green[1], green[0], 5, visitedColor)
    #c.pack()
    if pops == numberBeforeUpdate:
        c.update()
        pops = 0
    del hMap[place]
    closedSet[place] = parent
    possibilities = rails[place]
    for x in possibilities:
        if(goal==x):
            closedSet[x] = place
            showPath(goal, closedSet)
            notFound = False
            break
        elif x not in closedSet:
            newCost = cost+edgeToDistance[(place, x)]
            h = heuristic(x, goal, newCost)
            if not openSet.inThis(x):
                hMap[x] =h
                openSet.add((h, x, newCost, place))
            elif h<hMap[x]:
                hMap[x] =h
                openSet.update(x,h, place, newCost)
            blue = coordinates(nodesToCoordinates[x])
            create_circle(blue[1], blue[0], 5, fringeColor)
            
print(str(time.time() - initial)+" seconds to run")            
c.pack() 
c.mainloop()       

