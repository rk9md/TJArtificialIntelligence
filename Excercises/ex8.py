def removePunctuation(message):
    output = ""
    for x in message:
        if x.isalpha():
            output = output + x
    return output
import sys
message = str(sys.argv[1])
message = removePunctuation(message)
message = message.lower()
length = len(message)
if length%2==0:
    for x in range(0, int(length/2)):
        if message[x]!=message[length - x - 1]:
            print("Not a palindrome")
            break
        if(x==int(length/2)-1):
            print("Palindrome")
else:
    for x in range(0, int(length/2)+1):
        if message[x]!=message[length - x - 1]:
            print("Not a palindrome")
            break
        if(x==int(length/2)):
            print("Palindrome")