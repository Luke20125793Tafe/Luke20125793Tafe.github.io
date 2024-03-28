# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 16:54:45 2024

@author: Geektron

Exercise 1: Revise a previous program as follows: 
        Read and parse the “From” lines and pull out the addresses from the line. 
        Count the number of messages from each person using a dictionary.

After all the data has been read, print the person with the most commits by creating 
    a list of (count, email) tuples from the dictionary. 
    Then sort the list in reverse order and print out the person who has the most commits.
"""


emailCount = dict()


fileName = input('Enter a file name: ')

#QOL to check for .txt extension and add if missing
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
        #print(words)
        if words[1] not in emailCount:
            emailCount[words[1]] = 1
        else:
            emailCount[words[1]] = emailCount[words[1]] + 1

listFroms = list()
for key, val in list(emailCount.items()):
    listFroms.append((val, key))
    
listFroms.sort(reverse=True)

for key, val in listFroms[:1]:
    print(val, key)