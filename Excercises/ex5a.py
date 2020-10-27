import sys
num = int(sys.argv[1])
if num==1:
    print("Not Prime")
for x in range(2, int(num/2)+1):
    if num%x==0:
        print("Not Prime")
        break
    if x==int(num/2)+1:
        print("Prime")