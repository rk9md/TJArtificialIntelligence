import sys
maximum = ("", 0)
message = sys.argv[1]
for x in range(0, len(message)-1):
    diff = abs(ord(message[x]) - ord(message[x+1]))
    if diff > maximum[1]:
        maximum = (message[x]+message[x+1], diff)
print(maximum)