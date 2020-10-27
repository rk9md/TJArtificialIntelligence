import sys
message = sys.argv[1]
for x in set(message):
    if not (x=="1" or x=="0"):
        sys.exit(1)
print(int(sys.argv[1], 2))