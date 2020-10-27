import sys
import time
hexa = {"1":1, '2':2, '3':3, '4':4, '5':5, '6':6 ,'7':7 ,'8':8, '9':9, "a":10, 'b':11, "c":12, 'd':13, 'e':14, "f":15}
moves = {0:[1, 4], 1:[0, 2, 5], 2:[1, 3, 6], 3:[2, 7], 4:[0, 5, 8], 5:[1, 4, 6, 9], 6:[2, 5, 7, 10], 7:[3, 6, 11], 8:[4, 9, 12], 9:[5, 8, 10, 13], 10:[6, 9, 11, 14], 11:[7, 10, 15], 12:[8, 13], 13:[9, 12, 14], 14:[10, 13, 15], 15:[11, 14]}
sqrt= {0:0, 1:1, 4:2, 9:3, 2:1.414213, 5:2.36067, 10:3.162277, 8:2.828427, 13:3.605551, 18:4.242640}
goal = "123456789abcdef "

class Heap:
    
    def __init__(self):
        self.array = [(-1,"blank")]
        self.size = 0
    # def size(self):
    #     return self.size
    def swap(self, k, z):
        self.array[z], self.array[k]  = self.array[k], self.array[z]

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
        self.heapUp(self.size)
        
    def remove(self):
        self.swap(1, self.size)
        self.size-=1
        obj = self.array.pop()
        self.heapDown(1)
        return obj


def printstate ( currstate ):
    for r in range (4):
        for c in range (4):
            start = r*4+c
            print(currstate[start:start+1], end = "")
        print("\n", end="")
    print("\n")

def options ( currstate ):
    space = currstate.find(" ")
    possiblities = []
    
    for x in moves[space]:
        if space<x:
            possiblities.append( currstate[0:space] + currstate[x] + currstate[space+1:x] + currstate[space] + currstate[x+1:])
        else:
            possiblities.append( currstate[0:x] + currstate[space] + currstate[x+1:space] + currstate[x] + currstate[space+1:])
    return possiblities

def printSolution(sol, dict):
    steps = []
    while sol!="":
        steps.insert(0, sol)
        sol = dict[sol]
    for s in steps[1:]:
        printstate(s)
    print("Steps: "+str(len(steps)-1))

def inversionCount(curr):
    curr=curr.replace(" ", "")
    # count =0
    # for i in range(len(curr)-1):
    #     for j in range(i+1, len(curr)):
    #         if int(hexa[curr[i]])>int(hexa[curr[j]]):
    #             count+=1
    return len([1 for i in range(len(curr)-1) for j in range(i, len(curr)) if int(hexa[curr[i]])>int(hexa[curr[j]])])
def goalDict(goal):
    mymap = {}
    for z in range(len(goal)):
        mymap[goal[z]] = z
    return mymap
goalPlaces = goalDict(goal)

def distance(state, goal):
    total =0
    for x in range(len(state)):
        goalx = goalPlaces[state[x]]
        #if x==goalx: total+=1   #Number of tiles of of place
        #total+=sqrt[abs(x//4-goalx//4)**2+abs(x%4-goalx%4)**2]  #This is for eucleidan
        total+=abs(x//4-goalx//4)+abs(x%4-goalx%4)  #This is for Manhatten
    return total


pzlStates = 0
state = sys.argv[1].lower()
#state = '123456789abcdef '
state = state.translate({ord('_'): ' '})
rowSpacesaway = 3-state.find(" ")//4
#print(inversionCount(state))
printstate(state)
start = time.time()
if ((rowSpacesaway+inversionCount(state))&1==0):
    toBeParsed = Heap()
    toBeParsed.add((distance(state, goal), state, 0))
    alreadyParsed = {state:""}
    while(toBeParsed.size!=0):
        tub = toBeParsed.remove()
        pzlStates+=1
        curr = tub[1]
        move = tub[2]
        if(goal==curr):
            printSolution(curr, alreadyParsed)
            break
        possibilities = options(curr)
        for x in possibilities:
            if not x in alreadyParsed:
                toBeParsed.add((distance(x, goal)+(move+1), x, move+1))
                alreadyParsed[x] = curr
else:
    print("No Solution to this puzzle")
print(str(time.time()-start)+" seconds")
print(str(pzlStates)+" states removed before a solution was found")