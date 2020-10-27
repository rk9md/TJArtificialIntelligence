import sys
words = set(sys.argv[1].split(" "))
vowels = "aeiou"
for x in words:
    if x[0] in vowels and x[-1] in vowels:
        print(x)