import sys
message = sys.argv[1]
tried = {"", }
for x in range(0, len(message)):
    if message[x] not in message[x+1:] and message[x] not in tried:
        print(message[x])
        break
    tried.add(message[x])