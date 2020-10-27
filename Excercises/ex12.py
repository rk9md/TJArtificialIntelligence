import sys
num1 = int(sys.argv[1])
num2 = int(sys.argv[2])
for x in range(num1, num2+1):
    product = x**2 - 3*x + 2
    if x != num2:
        print(str(product)+", ", end = " ")
    else:
        print(str(product))