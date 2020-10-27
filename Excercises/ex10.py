def contains(num, list1):
    for x in list1:
        if x==num:
            return True
    return False
import sys
uniqueNums = []
sequence = []
arith = [int(o) for o in sys.argv[1:]]
for y in range(0, len(arith)):
    if not contains(arith[y], uniqueNums):
        uniqueNums.append(int(arith[y]))
diff = 0
found = False
for x in range(len(uniqueNums)):
    current = (x+1)%len(uniqueNums)
    diff = uniqueNums[current]-uniqueNums[x]
    check = True
    while current != (x-1)%len(uniqueNums):
        if diff != uniqueNums[(current+1)%len(uniqueNums)]-uniqueNums[current]:
            check = False
        current = (current+1)%len(uniqueNums)
    if(check):
        found = True
        #print("Yes: ", end=" ")
        start = (x+1)%len(uniqueNums)
        sequence.append(uniqueNums[x])
        #print(uniqueNums[x], end=" ")
        while start != x:
            #print(uniqueNums[start], end=" ")
            sequence.append(uniqueNums[start])
            start = (start+1)%len(uniqueNums)
        break
if found and contains(arith[0], sequence):
    first = sequence.index(arith[0])
    for x in arith:
        if x!=sequence[first]:
            print("No Arithmetic Sequence Found")
            sys.exit(0)
        first = (first+1)%(len(sequence))
    print("Yes: "+ " ".join([str(i) for i in sequence]))

else:
    print("No Arithmetic Sequence Found")