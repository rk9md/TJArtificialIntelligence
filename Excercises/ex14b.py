import sys
words = set(sys.argv[1].split(" "))
vowels = "aeiou"
for x in words:
    vow = 0
    for y in x:
        if y in vowels:
            vow+=1
    if vow>2:
        print(x)