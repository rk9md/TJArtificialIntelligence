import time, random
moves = {0:[1, 4], 1:[0, 2, 5], 2:[1, 3, 6], 3:[2, 7], 4:[0, 5, 8], 5:[1, 4, 6, 9], 6:[2, 5, 7, 10], 7:[3, 6, 11], 8:[4, 9, 12], 9:[5, 8, 10, 13], 10:[6, 9, 11, 14], 11:[7, 10, 15], 12:[8, 13], 13:[9, 12, 14], 14:[10, 13, 15], 15:[11, 14]}
goalPlaces = {"1":(0,0), '2':(0, 1), '3':(0, 2), '4':(0, 3), '5':(1, 0), '6':(1, 1) ,'7':(1, 2) ,'8':(1, 3), '9':(2, 0), "a":(2, 1), 'b':(2, 2), "c":(2, 3), 'd':(3, 0), 'e':(3, 1), "f":(3, 2)}
goals = {"1":1, '2':2, '3':3, '4':4, '5':5, '6':6 ,'7':7 ,'8':8, '9':9, "a":10, 'b':11, "c":12, 'd':13, 'e':14, "f":15}
absolute = {0:0, -1:1, -2:2, -3:3, 1:1, 2:2, 3:3}
rc = {0:(0,0), 1:(0, 1), 2:(0,2), 3:(0, 3), 4:(1, 0), 5:(1, 1), 6:(1, 2), 7:(1, 3), 8:(2, 0), 9:(2, 1), 10:(2, 2), 11:(2, 3), 12:(3, 0), 13:(3, 1), 14:(3, 2), 15:(3, 3)}
goal = "123456789abcdef "
start = time.time(); space = 15
def option( currstate ):
    n = random.randint(0, len(moves[space])-1)
    x = moves[space][n]
    second, first = rc[x], rc[space]
    goalx=goalPlaces[currstate[x]] 
    manChange = (absolute[first[0]-goalx[0]]+absolute[first[1]-goalx[1]]) - (absolute[second[0]-goalx[0]]+absolute[second[1]-goalx[1]])
    final = currstate
    one, two = final[space], final[x]
    final =final.replace(one, "*")
    final =final.replace(two, one)
    final =final.replace("*", two) 
    return (final, x, manChange)
curr = goal
sumOfMan, prevMan, n = 0, 0, 0
while time.time()-start<14.0:
    tup = option(curr)
    curr = tup[0]
    space = tup[1]
    prevMan+=tup[2]
    sumOfMan+=prevMan
    n+=1
totalTime = time.time()-start # insignificant time difference from the while
print(str(totalTime) + " seconds taken")
print("n: "+str(n))
print("Sum of Manhatten Distances/n: "+str(sumOfMan/n))
print("n/time: "+str(n/totalTime))
# time: 14.00018, n: 4004971, Sum of Manhatten Distances/n: 37.14652, n/time: 286065.6 