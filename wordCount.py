#! /usr/bin/env python3

import re

def createlist():
    ifile = input()
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

output = open("test.txt", "w")
wordList = createlist()

wordList.sort()
for x in wordList:
    output.write(x+"\n")
output.close()