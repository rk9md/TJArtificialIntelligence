import sys, time
hexa = {0:"0",1:"1", 2:"2", 3:"3", 4:"4", 5:"5", 6:"6" ,7:"7" ,8:"8", 9:"9", 10:"a", 11:'b'}
backhexa = {"0":0, "1":1, '2':2, '3':3, '4':4, '5':5, '6':6 ,'7':7 ,'8':8, '9':9, "a":10, 'b':11, "c":12, 'd':13, 'e':14, "f":15}

number = int(sys.argv[1])
indexToNeigh = {0:{1,2,3,4,5}, 1:{0,2,6,10,5}, 2:{0,1,6,3,7}, 3:{0,2,4,7,8}, 4:{0,3,5,8,9}, 5:{0,1,4,10,9}, 6:{11,10,7, 1, 2}, 7:{2,3,6,8,11}, 8:{3,4,7,9,11}, 9:{4,5,8,10,11}, 10:{1,5,6,9,11}, 11:{6,7,8,9,10}}
choices = {1,2,3,4,5,6,7,8,9,10,11}
def buildPuzzle(pzl, index):
    return pzl[0:index]+"X"+pzl[index+1:12]

def invalid(selects):
    new = backhexa[selects[-1]]
    for x in selects[:-1]:
        if new in indexToNeigh[backhexa[x]]:
            return True
    return False
def bruteForce(pzlTup):
    pzl = pzlTup[0]
    selected = pzlTup[1]
    count = len(selected)
    if invalid(selected):
        return ""
    if count==number:
        return pzl
    for x in choices:
        if hexa[x] not in selected:
            y = bruteForce((buildPuzzle(pzl, x), selected+hexa[x]))
            if y !="":
                return y
    return ""

def bruteForceColors(pzlTup):
    pzl = pzlTup[0]
    selected = pzlTup[1]
    count = len(selected)
    if invalid(selected):
        return ""
    for x in choices:
        if hexa[x] not in selected:
            y = bruteForceColors((buildPuzzle(pzl, x), selected+hexa[x]))
            if y !="":
                return y
    return (pzl, selected)



colorChoices = ["R", "B", "G", "Y"]
def matchedColors(pzl, curr):
    color = pzl[curr]
    for x in indexToNeigh[curr]:
        if color == pzl[x]:
            return True
    return False
finalpzl = ""
def bruteForceColors2(pzlTup):
    pzl = pzlTup[0]
    last = pzlTup[1]
    numColor = pzlTup[2]
    if matchedColors(pzl, last):
        return 5
    if last==11:
        #print(pzl)
        return numColor
    minimum = 5
    for x in colorChoices:
        if x not in pzl:
            numColor+=1
        minimum = min(minimum, bruteForceColors2((pzl[0:last+1]+x+pzl[last+2:12], last+1, numColor)))
    return minimum
start = time.time()
if int(number)<6:
    initial = 0 
    result = bruteForce((buildPuzzle("............", initial), str(initial)))
    if result!="":
        print(result)
        print("0123456789ab")
    else: 
        print("Not Possible")
    print(str(time.time()-start)+" seconds")
else: 
    print("Not Possible")
print(str(bruteForceColors2(("R...........", 0, 1)))+" colors")
