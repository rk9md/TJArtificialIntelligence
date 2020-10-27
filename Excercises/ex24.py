import sys
message = sys.argv[1].split(" ", 2)
print(message[2].replace(message[0], message[1]))