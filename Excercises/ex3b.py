import sys
div3 = []
for x in range(1, len(sys.argv)):
    if int(sys.argv[x])%3 == 0:
        div3.append(int(sys.argv[x]))
print(div3)