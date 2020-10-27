import sys
message = sys.argv[1]
out = ""
tried = {"", }
for x in message:
    if x not in tried:
        out+=x
    tried.add(x)
print(out)