#! /usr/bin/env python3

import re
import sys

if len(sys.argv) is not 3:
    print("Correct usage: wordCountTest.py <input text file> <output file>")
    exit()

ifile = sys.argv[1]
o = sys.argv[2]

def createlist():
    f = open(ifile, "r")
    words = list()

    #Read file line by line
    for line in f:
        line = line.strip()
        word = re.sub(r'[^\w\s]','', line)
        word = re.sub(r'\_','',word)
        word = re.split('[ \t]', word)
        #Append every word to one global list
        for cw in word:
            words.append(cw.lower())
    f.close()
    return words

def countwords(wordlist):
    output = open(o, "w")
    newwords = list()
    wordList.sort()
    for x in wordlist:
        if x not in newwords:
            newwords.append(x)
            count = wordlist.count(x)
            output.write(x + " " + str(count) + "\n")
    output.close()

wordList = createlist()
wordList = countwords(wordList)