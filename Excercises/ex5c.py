def isPrime(num):
    if(num==1)
        return false
    for x in range(2, int(num/2)+1):
        if num%x==0:
            return False
    return True
def primeBetween(num1, num2):
    for x in range(num1+1,num2):
        if isPrime(x):
            print(x, end = " ")
import sys
if len(sys.argv)-1==1:
    print(isPrime(int(sys.argv[1])))
if len(sys.argv)-1==2:
    primeBetween(int(sys.argv[1]), int(sys.argv[2]))