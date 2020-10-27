import sys
num1= 0
num2= 1
sum = 1
for x in range(0, int(sys.argv[1])):
    if x==0:
        print(1, end = "")
    else:
        sum = num1+num2
        print(", "+str(sum), end = "")
        num1 = num2
        num2= sum