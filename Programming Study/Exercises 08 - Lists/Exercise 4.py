# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 14:54:51 2024

@author: Geektron

Exercise 4: Find all unique words in a file

Shakespeare used over 20,000 words in his works. But how would you determine that? 
How would you produce the list of all the words that Shakespeare used? 
Would you download all his work, read it and track all unique words by hand?

Let’s use Python to achieve that instead. List all unique words, sorted in alphabetical order, 
    that are stored in a file romeo.txt containing a subset of Shakespeare’s work.

To get started, download a copy of the file www.py4e.com/code3/romeo.txt. 
Create a list of unique words, which will contain the final result. 
Write a program to open the file romeo.txt and read it line by line. 
For each line, split the line into a list of words using the split function. 
For each word, check to see if the word is already in the list of unique words. 
If the word is not in the list of unique words, add it to the list. 
When the program completes, sort and print the list of unique words in alphabetical order.
"""

fileName = input("Enter file: ")
openFile = open(fileName, 'r')

uniqueWords = []

for line in openFile:
    #print(line)
    words = line.split()
    for word in words:
        #print(word)
        if word in uniqueWords :
            continue
        else : 
            uniqueWords.append(word)

uniqueWords.sort(reverse=False)
print(uniqueWords)

#it is worth noting that this sorting goes by Capitalisation THEN by the starting letter
    