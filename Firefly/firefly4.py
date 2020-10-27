import math, random, time, itertools, sys, numpy
from tkinter import *

threshhold = .8
deltaX = 0.05
Tau = 2
circleRatio = 10
littleBit = 0.002

master= Tk()
c = Canvas(master, width=700, height=700, background="black")
c.pack()
buffer = 30
locationsToCoord = {x:(x//10,x%10) for x in range(100)}
coordinates = [[(buffer+random.uniform(50,650), buffer+random.uniform(50,650)) for c in range(10)] for r in range(10)]
def create_circle(numOfPoint, r, filler):
    j = locationsToCoord[numOfPoint]
    coorde = coordinates[j[0]][j[1]]
    y = coorde[1]
    x = coorde[0]
    c.create_oval(x-r, y-r, x+r, y+r, fill=filler)


fireflies = numpy.array([random.random() for x in range(100)])
#print(fireflies)
for _ in range(100):
    create_circle(_, circleRatio/2, "yellow")

def checkFlies(fireflies):
    bumped = set()
    try:
        c.delete("all")
        for x in range(len(fireflies)):
            if fireflies[x]<threshhold:
                color = hex(int(255*fireflies[x]))[2:]
                if len(color)!=2:
                    color = "0"+color
                create_circle(x, circleRatio*fireflies[x], "#"+color+color+"00")
            else:
                create_circle(x, circleRatio, "yellow")
            if fireflies[x]>threshhold:
                bumped.add(x)
                #numpy.add(fireflies,littleBit)
                for z in range(len(fireflies)):
                    if z not in bumped:
                        fireflies[z]+=littleBit
                fireflies[x]=0
            else:
                fireflies[x]+=(1-fireflies[x])*deltaX /Tau
        return fireflies
    except:
        return
c.focus_force()
def close(f):
    master.destroy()
master.bind("<Key>", close)

c.pack()
while True:
    fireflies = checkFlies(fireflies)
    try:
        master.update()
    except:
        break


c.mainloop()
