import sys
message = sys.argv[1].split(" ", 1)
count = 0
posistions = []
start = 0
while start<len(message[1]):
    index = message[1].find(message[0], start)
    if(index == -1):
        break
    posistions.append(index)
    count+=1
    start = index+1
print(str(count) + " (found at positions "+" and ".join(str(x) for x in posistions)+")")