import keras, random
from keras.models import Sequential
from keras.layers import Dense, Activation

import numpy
model = Sequential()
iteration = 2000
epochsI = 300

model.add(Dense(units=10, input_dim=3))
model.add(Activation('sigmoid'))
# model.add(Dense(units=8))
# model.add(Activation('sigmoid'))
model.add(Dense(units=1))
model.add(Activation('sigmoid'))

#model.add(Dense(units=1))
model.compile(loss='mse', optimizer="adam", metrics=['accuracy'])


def makeTestData():
    x = []
    y = []
    for _ in range(iteration//2):
        coordX = random.uniform(-1.5, 1.5)
        coordY = random.uniform(-1.5, 1.5)
        
        while coordX**2+coordY**2<1:
            coordX = random.uniform(-1.5, 1.5)
            coordY = random.uniform(-1.5, 1.5)
        x.append([coordX,coordY,1]) 
        y.append([0.0])
    for _ in range(iteration//2):
        coordX = random.uniform(-1.5, 1.5)
        coordY = random.uniform(-1.5, 1.5)
        
        while coordX**2+coordY**2>1:
            coordX = random.uniform(-1.5, 1.5)
            coordY = random.uniform(-1.5, 1.5)
        x.append([coordX,coordY,1]) 
        y.append([1.0])      
    x=numpy.array(x)
    y=numpy.array(y)
    return x, y

def makeExampleData():
    x = []
    y = []
    for _ in range(100000):
        coordX = random.uniform(-1.5, 1.5)
        coordY = random.uniform(-1.5, 1.5)
        x.append([coordX,coordY,1])
        if coordX**2+coordY**2<1:
            y.append([1.0])
        else:
            y.append([0.0])
    x=numpy.array(x)
    y=numpy.array(y)
    return x, y
x, y = makeTestData()
model.fit(x, y, batch_size = 1, epochs=epochsI)
#print(model.predict(x))

xTest, yTest = makeExampleData()
#####################################
#FIx
#####################################
numWrong = 0
yPred = model.predict(numpy.array(xTest))
for s in range(100000):
    if yPred[s][0]<0.5:
        result = 0
    else:
        result = 1
    if yTest[s][0]!=result:
        numWrong+=1
print(numWrong/10)

# print(model.get_weights())
