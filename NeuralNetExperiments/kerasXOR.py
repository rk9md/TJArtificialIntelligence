import keras, random
from keras.models import Sequential
from keras.layers import Dense, Activation

import numpy
model = Sequential()
iteration = 20000

model.add(Dense(units=2, input_dim=2))
model.add(Activation('sigmoid'))
model.add(Dense(units=1))
model.add(Activation('sigmoid'))
#model.add(Dense(units=1))
model.compile(loss='mse', optimizer="adam", metrics=['accuracy'])

x = numpy.array([[0.0,0.0],[0.0,1.0],[1.0,0.0],[1.0,1.0]])
y = numpy.array([[0.0],[1.0],[1.0],[0.0]])

model.fit(x, y, batch_size = 1, epochs=iteration)
print(model.predict(x))
summ = [0,0,0,0]
xTest = []
yTest = []
for s in range(iteration):
    curr = random.randint(0,3)
    xTest.append(x[curr])
    yTest.append(y[curr])
yPred = model.predict(numpy.array(xTest))
for s in range(iteration):
    f = int(xTest[s][0]*2+xTest[s][1])
    summ[f]+=((yTest[s][0]-yPred[s][0])**2)
errors = [l/2/iteration for l in summ]
print(errors)

print(model.get_weights())