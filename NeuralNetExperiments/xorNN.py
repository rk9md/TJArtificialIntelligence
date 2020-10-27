import sys, re, random, math, time
# random.seed(0)

iteration = 100000




numOfNodesinHiddenLayer = sys.argv[1]
textFile = sys.argv[2]
bias = 1

gradientScale = 0.1
# COLLECTING DATA
#################################################################################################################################
def extractNNSpecs():
    numOfNodesinHiddenLayer = sys.argv[1]
    textFile = sys.argv[2]
    Training = open(textFile, "r").read().splitlines()
    Initial, Final = [], []
    for x in Training:
        Initial.append([x[0], x[2], bias])
        Final.append([x[7]])
    numOfNodesInEachLayer = [len(Initial[0])] + [int(n) for n in sys.argv[1:-1]] + [len(Final[0])]
    return Initial, Final, numOfNodesInEachLayer

def extractNNSpecsG():
  args = sys.argv[1:]               # command line arguments
  if len(args)<1 or re.compile("^\\d+$").search(args[-1]) is not None:
    args += [sys.argv[0] + "..\\..\\XOR.txt"]   # append the ...
  fileLoc = args[-1]                # training set location
  aTraining = open(fileLoc, "r").read().splitlines()  # make a list of the training set
  aInitial, aFinal = [], []         # We'll separate the input and output
  for idx in range(len(aTraining)): # For each training set item
    strIn, strOut = aTraining[idx].split("=>")  # separate it into input and output
#  print ("'{}' ==> '{}'".format(strIn, strOut))
    aInitial.append([float(mynum) for mynum in re.split(  # make each input part numeric
      "\\s+,?\\s*|\\s*,?\\s+", strIn.strip())] + [bias])   # trailing element is bias
    aFinal.append  ([float(mynum) for mynum in re.split(  # make each output part numeric
      "\\s+,?\\s*|\\s*,?\\s+", strOut.strip())])
  # Fix the number of nodes per each layer
  aLayerCt = [len(aInitial[0])] + [int(n) for n in args[:-1]] + [len(aFinal[0])]
  return aInitial, aFinal, aLayerCt
#
#################################################################################################################################


#Squash
#################################################################################################################################
def squashMatrix(matrix):
    dim = shape(matrix)
    for r in range(dim[0]):
        for c in range(dim[1]):
            matrix[r][c] = squash(matrix[r][c])
    return matrix

def squash(x):
    #print(x)
    return 1/(1+math.e**(-1*x))

def squashDerivative(x):
    squashed = squash(x)
    return squashed*(1-squashed)
#################################################################################################################################


# Matrix
#################################################################################################################################

def makeMatrix(row, column):
    #return [[1 for c in range(column)] for r in range(row)]
    return [[random.random() for c in range(column)] for r in range(row)]
def getFromMatrix(row, column, matrix):
    return matrix[row][column]


# error = #length of three
#print avg error, and weights
def shape(matrix):
    return (len(matrix),len(matrix[0]))
def matmul(mat1, mat2):
    shape1 = shape(mat1)
    shape2 = shape(mat2)
    try:
        if shape1[1]!=shape2[0]:
            raise Exception
    except:
        print("Dimension Mismatch")
        return None
    newMat = makeMatrix(shape1[0],shape2[1])
    for r in range(shape1[0]):
        for c in range(shape2[1]):
            num = 0
            for x in range(shape1[1]):
                num+=(mat1[r][x]*mat2[x][c])
            newMat[r][c] = num
    return newMat

def subtractMatrix(mat1, mat2):
    s1 = shape(mat1)
    s2 = shape(mat2)
    try:
        if s1!=s2:
            raise Exception
    except:
        print("Dimension Mismatch")
        return None
    newMat = makeMatrix(s1[0], s1[1])
    for r in range(s1[0]):
        for c in range(s1[1]):
            newMat[r][c] = mat1[r][c] - mat2[r][c]
    return newMat

def addMatrix(mat1, mat2):
    s1 = shape(mat1)
    s2 = shape(mat2)
    try:
        if s1!=s2:
            raise Exception
    except:
        print("Dimension Mismatch")
        return None
    newMat = makeMatrix(s1[0], s1[1])
    for r in range(s1[0]):
        for c in range(s1[1]):
            newMat[r][c] = mat1[r][c] + mat2[r][c]
    return newMat
#################################################################################################################################
#################################################################################################################################

inputs, outputs, actNumOfNodesInEachLayer = extractNNSpecsG()
numOfNodesInEachLayer=actNumOfNodesInEachLayer+[1]
weights = [makeMatrix(numOfNodesInEachLayer[x],numOfNodesInEachLayer[x+1]) for x in range(len(numOfNodesInEachLayer)-1)] #List of Matrix
gradients = [makeMatrix(numOfNodesInEachLayer[x],numOfNodesInEachLayer[x+1]) for x in range(len(numOfNodesInEachLayer)-1)]
nodesX = [makeMatrix(1,x) for x in actNumOfNodesInEachLayer]#List of Matrix
#################################################################################################################################



#################################################################################################################################
# NOT GENERAL
#
#################################################################################################################################
#Forward Prop
#################################################################################################################################
def forwardProp(nodes,weights):
    for x in range(len(nodes)-1):
        # nodes[x+1] = matmul(nodes[x], weights[x])
        nodes[x+1] = squashMatrix(matmul(nodes[x], weights[x]))
    # final = matmul(nodes[-1], weights[-1])  
    final = squashMatrix(matmul(nodes[-1], weights[-1]))
    return nodes, final
#################################################################################################################################


#Back Prop
#################################################################################################################################
# def error(layer, i, nodes, weights, expected, answer): #TO MAKE FASTER STORE THE ERRORS CALCULATED
#     if layer==len(weights):
#         return (expected - answer[0][0])####### NOT GENERALIZED
#     #firstPart
#     summ = 0
#     for j in range(len(weights[layer][0])):
#         summ+=(weights[layer][i][j]*error(layer+1, j, nodes,weights, expected, answer))
#     #secondPart
#     fPrime  = squashDerivative(nodes[layer][0][i])
#     return summ*fPrime
def error(nodes, weights, expected, answer): #  NOT GENERAL
    errors = [makeMatrix(1,x) for x in numOfNodesInEachLayer]
    layer = len(errors)-1
    #print(layer)
    first = True
    while layer!=-1:
        if first:
            errors[layer][0][0] = (expected - answer[0][0])*squashDerivative(answer[0][0])*-1
            first=False #POSSIBLY FLIPPED
        else:
            for r in range(len(errors[layer])):
                for i in range(len(errors[layer][r])):
                    summ = 0
                    for j in range(len(weights[layer][0])):
                        summ+=(weights[layer][i][j]*errors[layer+1][0][j])
                    errors[layer][r][i] = summ*squashDerivative(nodes[layer][0][i])
        layer-=1
    return errors
def negGradient(i,j,layer,nodes,errors):
    return nodes[layer][0][i]*errors[layer+1][0][j]

#print(inputs, outputs, actNumOfNodesInEachLayer)

def backProp(nodes,weights, gradients, expected, answer):
    errors = error(nodes, weights, expected, answer)
    #print(errors)
    for layer in range(len(gradients)):
        for r in range(len(gradients[layer])):
            for c in range(len(gradients[layer][r])):
                gradients[layer][r][c] = gradientScale*negGradient(r,c,layer,nodes,errors)
    return gradients
#################################################################################################################################

# Training
#################################################################################################################################
curr = 0
for x in range(iteration):
    curr = random.randint(0,len(inputs)-1)
    #print(inputs[curr], outputs[curr])
    out = outputs[curr][0] ########NOT GENERAL, THIS OR ANYTHING WITH EXPECTED
    # print(weights)
    
    nodesX[0][0] = inputs[curr]
    nodesX, answer = forwardProp(nodesX, weights)
    gradients = backProp(nodesX, weights, gradients,out, answer)
    for x in range(len(weights)):
        weights[x] = addMatrix(weights[x],gradients[x])
    # curr+=1
    # if curr==len(inputs):
    #     curr=0
#################################################################################################################################
#Tester
#################################################################################################################################
def tester(weights):
    errors = [0,0,0,0] #NOT GENERAL
    for x in range(iteration):
        nodes = [makeMatrix(1,x) for x in actNumOfNodesInEachLayer]#List of Matrix
        curr = random.randint(0,len(inputs)-1)
        #print(inputs[curr], outputs[curr])
        out = outputs[curr][0] ########NOT GENERAL, THIS OR ANYTHING WITH EXPECTED
        # print(weights)
        
        nodes[0][0] = inputs[curr]
        nodes, answer = forwardProp(nodes, weights)
        print(answer)
        ind = int(inputs[curr][0]*2+inputs[curr][1])
        errors[ind] += ((out-answer[0][0])**2)/2
    avgE = [x/iteration for x in errors]
    return avgE

print(tester(weights))
print(weights)