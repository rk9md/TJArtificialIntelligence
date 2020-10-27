print("What is your name?")
name = input()
f = open("prev.txt", 'r+')
allNames = f.readline().split()
length = len(allNames)
if length>0:
    print("Previous User(s): " + str(allNames[-1]), end=" ")
else:
    print("Previous User(s): None")
f.write(name+" ")