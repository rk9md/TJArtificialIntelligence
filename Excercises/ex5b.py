def isPrime(num):
    for x in range(2, int(num/2)+1):
        if num%x==0:
            return False
    return True
import sys
for x in range(int(sys.argv[1])+1, int(sys.argv[2])):
    if isPrime(x):
        print(x, end = " ")