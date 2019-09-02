#! /usr/bin/env python3

inputFile = input()

outputFile = open("test.txt", "w")

f = open(inputFile, "r")

wordList = list()

i = 0

for x in f:
    outputFile.write(x)
    wordList.append(x)
    print(wordList[i])
    i += 1

f.close()
outputFile.close()