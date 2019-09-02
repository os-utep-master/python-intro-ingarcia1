#! /usr/bin/env python3

inputFile = input()

outputFile = open("test.txt", "w")

f = open(inputFile, "r")

for x in f:
    outputFile.write(x)
    print(x)

f.close()
outputFile.close()

