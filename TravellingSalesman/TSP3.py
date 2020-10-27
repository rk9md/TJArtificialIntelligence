import math, random, time, itertools, sys
from tkinter import *
start = time.time()
if len(sys.argv)==2:
    fileName = sys.argv[1]
else:
    fileName = "DAU.txt"
f = open(fileName, mode='r')
inp = f.read().split()
numOfNodes = int(inp[0])
edges= inp[1:]
locationsToCoord = {}
latitudes = []
longitudes = []
for x in range(numOfNodes):
    lat = float(edges[2*x+1])/1000
    longi = float(edges[2*x])/1000
    latitudes.append(lat)
    longitudes.append(longi)
    locationsToCoord[x] = (lat, longi)
#####################################################
# THE TXT FILE IS IN LONG,LAT
#####################################################
#####################################################
# DISTANCE NEEDS TO BE THE WEIRD WAY FROM RAILROAD
# def distance(here, there):
#     xDist = (here[0]-there[0])**2
#     yDist = (here[1]-there[1])**2
#     return (xDist+yDist)**0.5
#####################################################
#####################################################
# DISPLAY USING TKINTER                             
#####################################################
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

distances = [{z:distance(locationsToCoord[x], locationsToCoord[z]) for z in range(numOfNodes)} for x in range(numOfNodes)]
# ^^^^ distance is a list which includes dictionaries that for their specific index to every other
# example use for x to y: distances[x][y]
orderedDistances = [sorted([(distances[x][z], z) for z in range(numOfNodes) if z!=x])  for x in range(numOfNodes)]
#print(sorted([distances[0][x] for x in range(numOfNodes)]))
master= Tk()
scale = 400 if fileName.upper()=="KAD.TXT" else 150
buffer = 30
maxLong = max(longitudes)
minLong = min(longitudes)
maxLat = max(latitudes)
minLat = min(latitudes)
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
def create_circle(numOfPoint, r, filler):
    coorde = coordinates(locationsToCoord[numOfPoint])
    y = coorde[0]
    x = coorde[1]
    c.create_oval(x-r, y-r, x+r, y+r, fill=filler)
def makeLine(hereNode, thereNode, color):
    coorde = coordinates(locationsToCoord[hereNode])
    othercoord = coordinates(locationsToCoord[thereNode])
    c.create_line(coorde[1], coorde[0], othercoord[1], othercoord[0], fill=color, width=1)


def makeIdealOrder():
    sortedOrder = [-1]*numOfNodes
    sortedOrder[0] = 0
    sortedOrder[1] = orderedDistances[0][0][1]
    sortedOrder[-1] = orderedDistances[0][1][1]
    #print(orderedDistances[0][0], orderedDistances[0][1])
    used = {0,orderedDistances[0][0][1],orderedDistances[0][1][1]}
    currAt = 1
    while currAt!=numOfNodes-2:
        shortestPoss = orderedDistances[sortedOrder[currAt]]
        count = 0

        while shortestPoss[count][1] in used:
            count+=1
        sortedOrder[currAt+1] = shortestPoss[count][1]
        used.add(shortestPoss[count][1])
        currAt+=1
    return sortedOrder

def makeIdealOrder2():
    coordsInOrder = [(locationsToCoord[point][0],locationsToCoord[point][1],point) for point in range(numOfNodes)]
    coordsSorted = sorted(coordsInOrder)
    top = coordsSorted[:numOfNodes//2]
    bottom = coordsSorted[numOfNodes//2:]
    topOrdered = [(x[1], x[2]) for x in top]
    bottomOrdered = [(x[1], x[2]) for x in bottom]
    finalTop = [x[1] for x in sorted(topOrdered)]
    finalBottom = [x[1] for x in sorted(bottomOrdered)]
    order2 = finalTop+finalBottom[::-1]
    indexOf0 = order2.index(0)
    order2 = order2[indexOf0:]+order2[:indexOf0]
    return order2



# order = [*range(1,numOfNodes)]
#random.shuffle(order)
order = makeIdealOrder()[1:]
#order = [9, 13, 20, 28, 29, 31, 34, 36, 32, 33, 35, 30, 26, 27, 23, 21, 24, 25, 22, 19, 14, 12, 18, 17, 16, 15, 11, 10, 8, 7, 6, 5, 4, 2, 3, 1, 37]
if order[0]>order[-1]:
    order = order[::-1]
order = [0]+order
print(*order)
for x in range(numOfNodes):
    if order[x] in {}:
        create_circle(order[x], 10, "red")
    else:
        create_circle(order[x], 5, "black")
    makeLine(order[x-1], order[x], "red")
totalDistCovered = [distance(locationsToCoord[order[x-1]], locationsToCoord[order[x]]) for x in range(numOfNodes)]
print(sum(totalDistCovered),"km")
c.pack()

def intersect(a,b,c,d, sequence): #ALL PARAMETERS ARE INDEXES OF THE POINTS
    #print(a,b,c,d)

    point1 = sequence[a]
    unchange = True
    point2 = sequence[b]
    point3 = sequence[c]
    point4 = sequence[d]
    if distances[point1][point2]+distances[point3][point4] > distances[point1][point3]+distances[point2][point4]:
        if a==0:
            a = numOfNodes
        if b==0:
            b = numOfNodes
        if c==0:
            c = numOfNodes
        if d==0:
            d = numOfNodes
        sequence = sequence[:b]+(sequence[b:d][::-1])+sequence[d:]
        unchange = False
    #print(sequence)
    return unchange, sequence
    #SO IF YOU HAVE LINES FROM A TO B AND C TO D, CHECK IF THE DISTANCE BETWEEN A AND B IS SHORTER THAN A AND C, IF SO ITS UNCROSSED, OTHERWISE IT IS CROSSED 
#Un cross all the lines# display orgiinal then press a key and display the next one
lineIndexes = [(x-1, x) for x in range(numOfNodes)]
listofMods = [0 if x==numOfNodes else x for x in range(numOfNodes+1)]
def uncrossPath(sequence):
    lastChecked = -1
    while True:
        #print(lastChecked)
        for x in range(numOfNodes):
            pointUno = listofMods[x]
            pointDos = listofMods[x+1]
            unchanged = True
            for f in range(x+1, numOfNodes):
                pointTres = listofMods[f]
                pointQuatro = listofMods[f+1]
                result, sequence = intersect(pointUno,pointDos,pointTres,pointQuatro,sequence)
                #print(result)
                if not result:
                    return sequence
                unchanged = unchanged&result
            if not unchanged:
                lastChecked = x
                # print("changed")
            elif lastChecked==x:
                return sequence
        if lastChecked==-1:
            return sequence
def uncrossPathComplete(oldSequence):
    old = oldSequence
    sequence = uncrossPath(old)
    while old!=sequence:
        old = sequence.copy()
        sequence = uncrossPath(old)
    return sequence
def uncrossPathPerm(sequence):
    lastChecked = -1
    while True:
        #print(lastChecked)
        for x in range(numOfNodes):
            pointUno = listofMods[x]
            pointDos = listofMods[x+1]
            unchanged = True
            for f in range(x+1, numOfNodes):
                pointTres = listofMods[f]
                pointQuatro = listofMods[f+1]
                result, sequence = intersect(pointUno,pointDos,pointTres,pointQuatro,sequence)
                #print(result)
                unchanged = unchanged&result
            if not unchanged:
                lastChecked = x
                # print("changed")
            elif lastChecked==x:
                return sequence
        if lastChecked==-1:
            return sequence

#####################################################
# THE TXT FILE IS IN LONG,LAT
#####################################################
#####################################################
# DISTANCE NEEDS TO BE THE WEIRD WAY FROM RAILROAD
# def distance(here, there):
#     xDist = (here[0]-there[0])**2
#     yDist = (here[1]-there[1])**2
#     return (xDist+yDist)**0.5
#####################################################
#####################################################
# DISPLAY USING TKINTER                             
#####################################################
def close(f):
    master.destroy()
    start = time.time()
    # while time.time()-start<5:
    #     x = 1
master.bind("<Key>", close)
c.mainloop()



# coordsInOrder = [(locationsToCoord[point][0],locationsToCoord[point][1],point) for point in range(numOfNodes)]
# coordsSorted = sorted(coordsInOrder)
# top = coordsSorted[:numOfNodes//2]
# bottom = coordsSorted[numOfNodes//2:]
# topOrdered = [(x[1], x[2]) for x in top]
# bottomOrdered = [(x[1], x[2]) for x in bottom]
# finalTop = [x[1] for x in sorted(topOrdered)]
# finalBottom = [x[1] for x in sorted(bottomOrdered)]
# order2 = finalTop+finalBottom[::-1]
# toChange, order2 = intersect(finalBottom[-1], finalTop[0], finalTop[-1], finalBottom[0], order2)



# old = order
# order2 = uncrossPath(order)
# while old!=order2:
#     old = order2.copy()
#     order2 = uncrossPath(old)
order2 = uncrossPathComplete(order)
master2= Tk()
c = Canvas(master2, width=mapWidth, height=mapLength)
c.focus_force()
indexOf0 = order2.index(0)
order2 = order2[indexOf0:]+order2[:indexOf0]
printOutOrder = order2.copy()[1:]
if printOutOrder[0]>printOutOrder[-1]:
    printOutOrder = printOutOrder[::-1]
printOutOrder = [0]+printOutOrder
print(*printOutOrder)
#print(len(set(order2))-len(order2))
for x in range(numOfNodes):
    if order[x] in {}:
        create_circle(order[x], 10, "red")
    elif order[x] in {}:
        create_circle(order[x], 10, "purple")
    else:
        create_circle(order[x], 5, "black")
    makeLine(order2[x-1], order2[x], "red")
totalDistCovered = [distance(locationsToCoord[order2[x-1]], locationsToCoord[order2[x]]) for x in range(numOfNodes)]
print(sum(totalDistCovered),"km")
c.pack()
def close2(f):
    master2.destroy()
master2.bind("<Key>", close2)
print(time.time()-start,  "seconds")
c.mainloop()
#################################
#
#Use itertools
#
#
#
#################################
def distanceOfPerm(perm):
    pathLength = 0
    for x in range(len(perm)-1):
        pathLength+=distances[perm[x]][perm[x+1]]
    return pathLength
def distanceOfPath(perm):
    pathLength = 0
    for x in range(len(perm)):
        pathLength+=distances[perm[x]][perm[x-1]]
    return pathLength
########################################################
pointsBetweenAnchors = 8
########################################################

addingProperty = pointsBetweenAnchors+2
permToDistance = {}
def convPermToString(perm):
    return ".".join([str(x) for x in perm])
def splice(a, b, seq):
    if a<b:
        return seq[a:b]
    else:
        return seq[a:]+seq[:b]

def improvePathPerm(sequence):
    #sq = sequence*2
    lastChange = -1
    while True:
        sequence = uncrossPath(sequence)
        for x in range(numOfNodes):
            starting = splice(x, (x+addingProperty)%numOfNodes, sequence) #sq[x:x+addingProperty]
            permList = list(itertools.permutations(starting[1:addingProperty-1]))
            permList2 = [[starting[0],*x, starting[-1]] for x in permList]
            permStringList = [convPermToString(x) for x in permList2]
            #print(permList)
            finals = []
            for s in range(len(permList)):
                if permStringList[s] not in permToDistance:
                    permToDistance[permStringList[s]] = distanceOfPerm(permList2[s])
                distance = permToDistance[permStringList[s]]
                # if distance == 0:
                #     print(permStringList[s])
                finals.append((distance, s, permStringList[s]))
            fastest = sorted(finals)[0]
            # if starting[0]==10:
            #     print(finals, fastest)
            # print(fastest)
            if fastest[1]!=0:
                # breakInterupt = numOfNodes-x
                # if breakInterupt>addingProperty-1:
                #     sequence[x:] = [*fastest[0]]
                # else:
                #     sequence[x:] = fastest[0][:breakInterupt]
                #     sequence[:(x+addingProperty)%numOfNodes] = fastest[0][breakInterupt:]
                spaces = numOfNodes-x-1
                pointsList = [*permList[fastest[1]]]
                #print(starting, pointsList)
                if spaces>pointsBetweenAnchors:
                    sequence[x+1:x+addingProperty-1] = pointsList
                else:
                    sequence[x+1:] = pointsList[:spaces]
                    sequence[:(x+addingProperty)%numOfNodes-1] = pointsList[spaces:]
                lastChange = x
            elif lastChange==x:
                return sequence
            # print(lastChange, x)
        if lastChange==-1:
            return sequence
            #print(sequence, sequence[x], distanceOfPath(sequence))           
#order2 = [0, 1, 3, 2, 4, 5, 6, 10, 11, 16, 18, 17, 15, 8, 7, 12, 14, 19, 22, 25, 24, 21, 23, 27, 26, 30, 35, 33, 32, 37, 36, 34, 31, 29, 28, 13, 20, 9]
oldOrder = order2

order3 = improvePathPerm(order2)
order3 = uncrossPathPerm(order3)
while oldOrder!=order3:
    oldOrder = order3.copy()
    order3 = improvePathPerm(oldOrder)
    order3 = uncrossPathPerm(order3)

master3= Tk()
c = Canvas(master3, width=mapWidth, height=mapLength)
c.focus_force()
indexOf0 = order3.index(0)
order3 = order3[indexOf0:]+order3[:indexOf0]
printOutOrder = order3.copy()[1:]

if printOutOrder[0]>printOutOrder[-1]:
    printOutOrder = printOutOrder[::-1]
printOutOrder = [0]+printOutOrder
print(*printOutOrder)

for x in range(numOfNodes):
    if order[x] in {}:
        tempColor = "purple"
    elif order[x] in {}:
        tempColor = "red"
    else:
        tempColor = "black"

    create_circle(order[x], 5, tempColor)
    makeLine(order3[x-1], order3[x], "red")

totalDistCovered = [distance(locationsToCoord[order3[x-1]], locationsToCoord[order3[x]]) for x in range(numOfNodes)]
print(sum(totalDistCovered),"km")
# print(permToDistance["10.18.17.16.15.11.8"])
# print(permToDistance["10.11.16.18.17.15.8"])
c.pack()
def close3(f):
    master3.destroy()
master3.bind("<Key>", close3)
# c.mainloop()
print(time.time()-start,  "seconds")