import sys
message = str(sys.argv[1])
output = ""
for x in message:
    if x.isalpha():
        output = output + x
print(output)