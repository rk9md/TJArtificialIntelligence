import sys
side1 = int(sys.argv[1])
side2 = int(sys.argv[2])
side3 = int(sys.argv[3])
halfPeri = (side1+side2+side3)/2
area = (halfPeri*(halfPeri-side1)*(halfPeri-side2)*(halfPeri-side3))**(1/2)
print(area)