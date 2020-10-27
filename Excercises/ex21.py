import sys
message = sys.argv[1].lower()
for x in set(message):
    if not (x=="1" or x=="0" or x=='a' or x=="c" or x=="d" or x=='e' or x=='f' or x=='b'):
        sys.exit(1)
print(int(sys.argv[1], 16))