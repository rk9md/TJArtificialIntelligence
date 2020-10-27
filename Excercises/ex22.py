import sys
message = sys.argv[1].split()
out = ""
for x in message:
    out+=x[::-1]+" "
print(out)