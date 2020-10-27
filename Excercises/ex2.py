import sys
messageIn = sys.argv[1]
messageOut = ""
for x in messageIn[::2]:
    messageOut+=x
print(messageOut)
