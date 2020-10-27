def removePunctuation(message):
    output = ""
    for x in message:
        if x.isalpha():
            output = output + x
    return output

import sys
vowels = "aeiou"
vowelcount = [0, 0, 0, 0, 0]
message = sys.argv[1]
message = removePunctuation(message)
for x in range(len(vowels)):
    for y in message:
        if vowels[x]==y:
            vowelcount[x] = vowelcount[x]+1
    print(str(vowels[x])+":"+str(vowelcount[x]), end = " ")

        