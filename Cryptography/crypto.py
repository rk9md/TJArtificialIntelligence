#################################################################################################################################################
# 4/25/18
# Dr. Gabor,
# This file is the updated version of my cryptogram program.
# I talked to you about the minor change I made that corrected line 150.
# The line orginally was if actualLetter in set(code) and decoded[letterToPosition[codedLetter]] !=actualLetter:
# This line was supposed to prevent a letter for being coded by two different letters. For example: X coding for A and B coding for A.
# What is wrong is that the variable code should be decoded. Code was the mapping for the puzzle before BruteForce but decoded was the mapping at each level.
# This caused the code to use a old version of the mapping and did not prevent the duplicates.
# The line has been fixed to if actualLetter in set(decoded) and decoded[letterToPosition[codedLetter]] !=actualLetter:
#################################################################################################################################################

import sys, re, time, string
start = time.time()
crypto = []
cString = ""
if len(sys.argv)==2:
    cString = sys.argv[1].upper()
    cString = ''.join([x for x in cString if x not in string.punctuation])
    crypto = cString.split()
else:
    crypto = sys.argv[1:] #List of all the words STATIC
    crypto = [''.join([x for x in z if x not in string.punctuation]).upper() for z in crypto]
    #crypto = ["TROPHOBIOSIS"]
    cString = " ".join(crypto).upper() #Coded String STATIC
#####################################
#        REMOVE PUNCTUATION         #
#     EVERYWHERE EVEN IN CRYPTO     #
#   REMEMBER TO ADD BACK THE PUNCT  #
#              IN FINAL             #
#####################################



deString = "" # STRING DECODED IS NON STATIC
decrpyt = crypto.copy()
wordsDone = "0"*len(crypto)
for x in crypto:
    deString +="."*len(x)+" "
lettersLeft = len(set(cString)-{" "})



alpha = "abcdefghijklmnopqrstuvwxyz ".upper()
code = "*"*26+" " #String that represents what each letter represents EX: If code has a G at the start, A codes to G NONSTATIC

numOfLetters = len(set(cString))


letterToPosition= {letter:x for x,letter in enumerate(alpha)} #Enter coded letter and returns position in alphabet STATIC

locations = {x:set() for x in alpha} #Where each letter is location STATIC

for z, letter in enumerate(cString):
    locations[letter].add(z)

freq = {letter:len(locations[letter]) for letter in alpha} #How often each letter occurs STATIC

wordLengths = [len(x) for x in crypto] #Lengths of each coded word in order STATIC
wordStartsAt  = []

wordToIndex = {x:ind for ind, x in enumerate(crypto)}



count = 0
for x in wordLengths:
    wordStartsAt.append(count)
    count+=x+1

def stringGetWord(string, index):  #the index is the index of the word in crpyto
    return string[wordStartsAt[index]:wordStartsAt[index]+wordLengths[index]]

wordLengthToWord = {}  #Maps lengths to each coded word STATIC

for x, num in enumerate(wordLengths):
    if num not in wordLengthToWord:
        wordLengthToWord[num]=set()
    wordLengthToWord[num].add(crypto[x]) 


mostCommonLetters= "etaoinshrdlu"

def wordPattern(word):
    pat = []
    count = 0
    seen = {}
    for x in word:
        if x not in seen:
            seen[x]=str(count)
            count+=1
        pat.append(seen[x])
    return ".".join(pat)



with open("scrabble.txt", mode='r') as f: scrabbleWords = {x.upper() for x in f.read().split() if re.search(r'^(((?=\w*[aeiouy])(a|[a-z]{2,}))|(?=\w*w)(?!\w*[aeiouy])([a-z]{2,}))$', x.lower())}
scrabbleWords.add("I")
scrabbleWords.add("A")

########################################################################
#TURNS ALL SCRABBLE WORDS IN TO PATTERNS AND PATTERNS INTO SETS OF WORDS
wordsToPatterns = {x:wordPattern(x) for x in scrabbleWords}  # Maps all words in scrabble words to their pattern STATIC
patternsToWords = {} # Maps all patterns to their potential words STATIC
for x in scrabbleWords: 
    pat = wordsToPatterns[x]
    if pat not in patternsToWords:
        patternsToWords[pat]=set()
    patternsToWords[pat].add(x)

########################################################################
f.close()
count = 0
f = open("count_1w.txt", mode='r')
commonity = f.read().upper().split()
commonWords = {}
for x in range(len(commonity)):
    if commonity[x] in scrabbleWords:
        commonWords[commonity[x]] = count
        count+=1
      



patternsOfWords = [wordPattern(x) for x in crypto] #Patterns of all of the words in puzzle in their place STATIC
possWords = [patternsToWords[patternsOfWords[x]] for x in range(len(crypto))] #A list in order of the possible words the pattern could be STATIC
numOfPossWords = [len(x) for x in possWords] # A list of the number of words each coded word pattern STATIC
dictPossWords = {} #Basically the list above just as a dictoinary of legnth to a set of words STATIC
for x, word in enumerate(crypto):
    if numOfPossWords[x] not in dictPossWords:
        dictPossWords[numOfPossWords[x]] = set()
    dictPossWords[numOfPossWords[x]].add(word)

numberOfPossWordsInOrder = sorted(dictPossWords)



#print(numOfPossWords)
#IF THERE IS ONLY ONE LETTER IN THE WORD
#IF THERE IS ONLY ON WORD FOR A PATTERN
        #SO GET ALL THE PATTERNS FOR THE WORDS AND RUN THEIR LENGTHS
#GO FROM THE MOST OCCURING TO THE LEAST AND USE FREQUENCY TO GUESS
#So When you get a word that has letters solved in it, re match through the list 
def guessWord(decodedString, decoded, codeWord, actualWord, count):
    newString = list(decodedString)
    newDecoded = list(decoded)
    newCount = count
    for x in range(len(codeWord)):
        codedLetter = codeWord[x]
        actualLetter = actualWord[x]
        if actualLetter in set(decoded) and decoded[letterToPosition[codedLetter]] !=actualLetter:
            return None, None, None
        if newDecoded[letterToPosition[codedLetter]] =="*":
            for z in locations[codedLetter]:
                newString[z] = actualLetter
            newDecoded[letterToPosition[codedLetter]] = actualLetter
            newCount-=1
    #   DONT TURN CODE INTO A LIST, NEEDS TO BE STRING TO MAINTAIN UNIQUE
    return "".join(newString), "".join(newDecoded), newCount

def guessLetter(decodedString, decoded, codedLetter, actualLetter):
    # for x in locations[codedLetter]:
    #     decodedString = decodedString[0:x] + actualLetter + decodedString[x+1:]
    ######################################
    #    TEST TO SEE WHICH IS FASTER     #    
    ######################################
    newString = list(decodedString)
    for x in locations[codedLetter]:
         newString[x] = actualLetter
    #   DONT TURN CODE INTO A LIST, NEEDS TO BE STRING TO MAINTAIN UNIQUE
    return "".join(newString), decoded[:letterToPosition[codedLetter]]+actualLetter+decoded[letterToPosition[codedLetter]+1:]



# lettersLeft = "abcdefghijklmnopqrstuvwxyz"

if numberOfPossWordsInOrder[0] == 1: #IF THERE EVEN IF A WORD WITH JSUT ONE POSSIBILITY
    for x in dictPossWords[1]: #GO THROUGH ALL THE ONE LEGNTH WORDS
        actualWord = [*patternsToWords[wordPattern(x)]][0]
        deStringN, codeN, lettersLeftN = guessWord(deString, code, x, actualWord, lettersLeft)
        if deStringN:
            deString, code, lettersLeft = deStringN, codeN, lettersLeftN

        wordsDone=wordsDone[:wordToIndex[x]]+"1"+wordsDone[wordToIndex[x]+1:]


def matchOnSet(reString, set):
    finalSet = {x for x in set if re.match(reString, x)}
    return finalSet

# PRIORITYQUEUE = []
# if 1 in wordLengthToWord:
#     for x in wordLengthToWord[1]: #Adding all one length words
#         PRIORITYQUEUE.append(x)
# for x in numberOfPossWordsInOrder: #adding the letters in order of the least amount of words possible for a word
#     if x!=2 or x!=1:
#        for z in dictPossWords[x]:
#            for y in set(z):
#                if y not in set(PRIORITYQUEUE):
#                    PRIORITYQUEUE.append(y)

def isRight(decodedString, wordsDone):
    possWords = {}
    newWords = list(wordsDone)
    for x in range(len(crypto)):
        word = stringGetWord(decodedString, x)
        pattern = patternsOfWords[x]
        finalSet = matchOnSet("^"+word+"$", patternsToWords[pattern])
        
        if len(finalSet)==0:
            return False, None, None
        if "." not in set(word):
            newWords[x] = "1"
        else:
            possWords[x]=(finalSet)
    return True, possWords, newWords 
# def reverseDictionary(d):
#     newD = {}
#     for x in d:
#         if 

def sortSetbyCommon(posswords):
    tupleList = []
    for x in posswords:
        if x in commonWords:
            tupleList.append((commonWords[x], x))
        else:
            tupleList.append((90000, x))
    finalList = sorted(tupleList)
    finalList = [x[1] for x in finalList]
    return finalList

allPossCryptos = set()
def recurThroughPoss(deString, code, count, wordsDone):
    works, possWords, newWordsDone = isRight(deString, wordsDone)
    if not works:
        return None
    elif count==0:
        #allPossCryptos.add(deString)
        return deString
    else:
        lengthsInOrder = sorted([(len(possWords[x]), x) for x in possWords]) #Contains tuples of len of possWords set and its position
        for z in lengthsInOrder:
            currIndex = z[1]
            guessList = possWords[currIndex]
            guessList = sortSetbyCommon(guessList)
            for guess in guessList:                
                guessedDeString, guessedCode, guessCount = guessWord(deString, code, stringGetWord(cString, currIndex), guess, count)
                if guessedDeString:
                    answer = recurThroughPoss(guessedDeString, guessedCode, guessCount, newWordsDone)
                    if answer:
                        return answer





print(recurThroughPoss(deString, code, lettersLeft, wordsDone))

#print(allPossCryptos, deString, lettersLeft)
#if allPossCryptos:
#   print(list(allPossCryptos)[0])


print(time.time()-start)