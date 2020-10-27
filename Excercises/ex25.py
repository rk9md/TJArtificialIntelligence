import sys
def letterCount(s):
    letters = {}
    for x in s:
        if x in letters:
            letters[x] = letters[x] + 1
        else:
            letters[x] = 1
    return letters
first = letterCount(sys.argv[1])
second = letterCount(sys.argv[2])
if len(first)==len(second):
    for x in first:
        if x not in second or first[x]!=second[x]:
            print("Not Anagrams")
            sys.exit(1)
else:
    print("Not Anagrams")
    sys.exit(1)
print("They are Anagrams")

