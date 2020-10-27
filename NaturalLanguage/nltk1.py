from nltk.book import text1


f = open("wordss.txt", mode='r')
dictionary = f.read().split()
f.close()
majorCorpus = text1
f = open("recentPaper.txt", mode='r')
myRecent = f.read().split()
f.close()
f = open("oldPaper.txt", mode='r')
myOld = f.read().split()
f.close()
lits = [dictionary, majorCorpus, myRecent, myOld]
titles = ["The dictionary", "Moby Dick by Herman Melville", "My recent paper", "My old paper"]
print()
for z in range(4):
    literature = lits[z]
    title = titles[z]
    #Number of Words
    print(title+" had {} words total".format(len(literature)))
    #Number of Unique Words
    uniq = len(set(literature))
    print("It had {} unique words".format(uniq))
    #Average Length of Unique Words
    uniqLen = 0
    print(sum([len(i) for i in set(literature)])/len(set(literature)))
    for x in set(literature):
        uniqLen+=len(x)
        # uniqLen-=(x.count("-"))
        # uniqLen-=(x.count("'"))
    print("The average length of the unique words was {} letters".format(uniqLen/uniq))
    #Average Number of Vowels in Uniq
    vowels = 0
    for x in set(literature):
        for y in x:
            if y.lower() in {"a", "e", "i", "o", "u", "y"}:
                vowels+=1
    print("The average number of vowels in a unique word is {} vowels".format(vowels/uniq))
    print()