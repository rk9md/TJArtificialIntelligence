import re
# f = open("wordsss.txt", mode='r')
# dictionary = f.read().split()
# f.close()
#scrabbleWords = {x for x in dictionary if re.search(r'^(a|[a-z]{2,})$', x)}
with open("wordsss.txt", mode='r') as f: scrabbleWords = {x for x in f.read().split() if re.search(r'^(((?=\w*[aeiouy])(a|[a-z]{2,}))|(?=\w*w)(?!\w*[aeiouy])([a-z]{2,}))$', x)}
lengthOf3 = {x for x in scrabbleWords if len(x)>2}
lengthOf4 = {x for x in scrabbleWords if len(x)>3}
prefix3 = {x[0:3] for x in lengthOf3}
prefix4 = {x[0:4] for x in lengthOf4}
for x in scrabbleWords:
    if re.search(r'^(?=\w*w)(?!\w*[aeiouy])([a-z]{2,})$', x):
        print(x)

# for x in dictionary:
#     if re.search(r'^(a|[a-z]{2,})$', x):
#         scrabbleWords.add(x)
#         #lengthOf3 = {x for x in scrabbleWords if len(x)>2}
#         #lengthOf4 = {x for x in scrabbleWords if len(x)>3}
#         if len(x)>=3: #if re.search(r'^[a-z]{3,}$', x):
#             lengthOf3.add(x)
#         if len(x)>=4: #if re.search(r'^[a-z]{4,}$', x):
#             lengthOf4.add(x)
# prefix3=set() #{x[0:3] for x in lengthOf3 if len(x)>2}
# prefix4 = set() #{x[0:4] for x in lengthOf4}
# for x in lengthOf3: 
#     if x[0:3] not in prefix3:
#         prefix3.add(x[0:3])

# for x in lengthOf4:
#     if x[0:4] not in prefix4:
#         prefix4.add(x[0:4])

print("Number of scrabble words: {}".format(len(scrabbleWords)))
print("Number of scrabble words with 3 or more letters: {}".format(len(lengthOf3)))
print("Number of scrabble words with 4 or more letters: {}".format(len(lengthOf4)))
print("Number of unique 3 letter prefixes: {}".format(len(prefix3)))
print("Number of unique 4 letter prefixes: {}".format(len(prefix4)))
