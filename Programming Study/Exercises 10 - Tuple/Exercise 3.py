# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 17:54:45 2024

@author: Geektron

Exercise 3: Write a program that reads a file and prints the letters in decreasing order of frequency.

Your program should convert all the input to lower case and only count the letters a-z. 
Your program should not count spaces, digits, punctuation, or anything other than the letters a-z. 
Find text samples from several different languages and see how letter frequency varies between languages. 
"""

import string

fileName = input('Enter a file name: ')

#QOL to check for .txt extension and add if missing
if fileName.find(".txt") == -1:
    fileName = fileName + '.txt'

openFile = open(fileName)

letterCount = dict()

for line in openFile:
    line = line.rstrip()
    line = line.translate(line.maketrans('', '', string.digits))
    line = line.translate(line.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        #print(word)
        #print(letters)
        for letter in word:
            if letter not in letterCount:
                letterCount[letter] = 1
            else:
                letterCount[letter] = letterCount[letter] + 1
            
letterList = list()

for key, val in list(letterCount.items()):
    letterList.append((key, val))
    
letterList.sort(reverse=False)

for key, val in letterList:
    print(key, val)