import sys
from tkinter import *
import math
import time
def toRadians(num):
    return num*math.pi/180
def distance(here, there):
    r = 6371.008 #km
    #r = 3959 #miles
    la1 = toRadians(here[0])
    la2 = toRadians(there[0])
    dLo = toRadians(there[1])- toRadians(here[1])
    dLa = la2-la1 
    a = math.sin(dLa/2)*math.sin(dLa/2) + math.cos(la1)*math.cos(la2) * math.sin(dLo/2)*math.sin(dLo/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    return r*c
start = time.time()
prefix = "rom"
f = open(prefix+"Nodes.txt", mode='r')
citiesToID = {}
idToCities = {}
nodesToCoordinates = {}
rails = {}
RomNames={}
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
    edgeToDistance[(edges[x], edges[x+1])] = distance(nodesToCoordinates[edges[x]], nodesToCoordinates[edges[x+1]])
e.close()
n = open("romFullNames.txt")
names = n.read().split()
for x in range(len(names)):
    RomNames[names[x][0]]=x
n.close()

master= Tk()
scale = 150
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


c = Canvas(master, width=mapWidth, height=mapLength)
c.pack()

alreadySeen = set()
parsing = {nodes[0]}
while len(parsing)!=0:
    curr = parsing.pop()
    coord = coordinates(nodesToCoordinates[curr])
    for x in rails[curr]:
        if x not in alreadySeen:
            otherCoord = coordinates(nodesToCoordinates[x])
            #print(nodesToCoordinates[curr], nodesToCoordinates[x])
            c.create_line(coord[1], coord[0], otherCoord[1], otherCoord[0])
            parsing.add(x)
    alreadySeen.add(curr)


#print(distance((50, -5), (58, -3)))
dist = 0
for x in edgeToDistance:
    dist+=edgeToDistance[x]
print("Total Distance is "+str(dist) + " kilometers")
c.create_line(0,0,10,10)
print(str(time.time()-start)+" seconds")
mainloop()