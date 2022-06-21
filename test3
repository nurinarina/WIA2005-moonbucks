# Tokenizing the data
import re

# Setting up data\


def text_analysis(text):
    with open(text) as f:
        contents = f.read().lower()

# opening a text file
    file1 = open("positive.txt", "r")
    lines = file1.read().splitlines()
    file1.close()

    file2 = open("negative.txt", "r")
    lines1 = file2.read().splitlines()
    file1.close()

    theTokens = re.findall(r'\b\w[\w-]*\b', contents.lower())
#print(theTokens[:5])


# Calculating positive words
    numPosWords = 0
    for word in theTokens:
        if word in lines:
            numPosWords += 1
    print("Number of positive words: " + str(numPosWords))

# Calculating negative words

    numNegWords = 0
    for word in theTokens:
        if word in lines1:
            numNegWords += 1
    print("Number of negative words: " + str(numNegWords))


# Deciding positive or negative
    if numPosWords > numNegWords:
        print("Positive " + str(numPosWords) + ":" + str(numNegWords))
        print(1)
    elif numNegWords > numPosWords:
        print("Negative " + str(numPosWords) + ":" + str(numNegWords))
        print(1)
    elif numNegWords == numPosWords:
        print("Neutral " + str(numPosWords) + ":" + str(numNegWords))
        print(1)

    print()
