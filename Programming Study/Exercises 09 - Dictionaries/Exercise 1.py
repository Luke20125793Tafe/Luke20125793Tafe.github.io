# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 16:12:38 2024

@author: Geektron

Write a program that reads the words in words.txt and stores them as keys in a dictionary. 
It doesn’t matter what the values are. 
Then you can use the in operator as a fast way to check whether a string is in the dictionary.
"""

wordDict = dict()
openFile = open('words.txt')

for line in openFile :
    words = line.split()
    for word in words:
        print(word)
        if word in wordDict :
            continue
        else :
            wordDict[word] = word
            
print(wordDict)
    