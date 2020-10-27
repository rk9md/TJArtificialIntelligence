import sys, time
hexa = {0:"0",1:"1", 2:"2", 3:"3", 4:"4", 5:"5", 6:"6" ,7:"7" ,8:"8", 9:"9", 10:"a", 11:'b', 12:"c", 13:"d", 14:"e", 15:"f", 16:"g", 17:"h", 18:"i", 19:"j"}
backhexa = {"0":0, "1":1, '2':2, '3':3, '4':4, '5':5, '6':6 ,'7':7 ,'8':8, '9':9, "a":10, 'b':11, "c":12, 'd':13, 'e':14, "f":15, "g":16, "h":17, "i":18, "j":19}

#number = int(sys.argv[1])
indexToNeigh = {0:{10,1,19}, 1:{0,2,8}, 2:{1,3,6}, 3:{2,19,4}, 4:{3,17,5}, 5:{6,15,4}, 6:{2,5,7}, 7:{8,14,6}, 8:{7,9,1}, 9:{13,8,10}, 10:{9,11,0}, 11:{10,12,18}, 12:{16,13,11}, 13:{14,9,12}, 14:{7,13,15}, 15:{16,14,5}, 16:{15,12,17}, 17:{18,16,4}, 18:{19,11,17}, 19:{0,3,18}}
choices = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19}
def buildPuzzle(pzl, index):
    return pzl[0:index]+"X"+pzl[index+1:20]

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
        if x>len(pzl):
            print("Nope")
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
    if last==19:
        if numColor==3:
            print(pzl)
        return numColor
    minimum = 5
    for x in colorChoices:
        if x not in set(pzl):    
            minimum = min(minimum, bruteForceColors2((pzl[0:last+1]+x+pzl[last+2:20], last+1, numColor+1)))
        else:
            minimum = min(minimum, bruteForceColors2((pzl[0:last+1]+x+pzl[last+2:20], last+1, numColor)))

    return minimum

start = time.time()
# if int(number)<20:
#     initial = 0 
#     result = bruteForce((buildPuzzle("....................", initial), str(initial)))
#     if result!="":
#         print(result)
#         print("0123456789abcdefghij")
#     else: 
#         print("Not Possible")
#     print(str(time.time()-start)+" seconds")
# else: 
#     print("Not Possible")
print(str(bruteForceColors2(("R...................", 0, 1)))+" colors")
