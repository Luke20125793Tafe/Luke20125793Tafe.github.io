# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 16:57:51 2024

@author: Geektron

Exercise 3: Write a program to read through a mail log, build a histogram using a dictionary
    to count how many messages have come from each email address, and print the dictionary.
"""

fromCount = dict()

fileName = input('Enter a file name: ')
extenCheck = fileName.find(".txt")
if extenCheck == -1:
    fileName = fileName + '.txt'
    
openFile = open(fileName)

for line in openFile :
    words = line.split()
    #print('Debug:', words)
    if len(words) < 2 or words[0] != 'From' : 
        continue
    else:
        emailFrom = words[1]
        if emailFrom not in fromCount:
            fromCount[emailFrom] = 1
        else:
            fromCount[emailFrom] = fromCount[emailFrom] + 1

print(fromCount)