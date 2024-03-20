# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 15:33:09 2024

@author: Geektron

Exercise 5: Minimalist Email Client.

MBOX (mail box) is a popular file format to store and share a collection of emails. 
This was used by early email servers and desktop apps. 
Without getting into too many details, MBOX is a text file, which stores emails consecutively. 
Emails are separated by a special line which starts with From (notice the space). 
Importantly, lines starting with From: (notice the colon) describes the email itself 
    and does not act as a separator. 
Imagine you wrote a minimalist email app, that lists the email of the senders in 
    the user’s Inbox and counts the number of emails.

Write a program to read through the mail box data and when you find line that starts with “From”, 
    you will split the line into words using the split function. 
We are interested in who sent the message, which is the second word on the From line.

You will parse the From line and print out the second word for each From line, 
    then you will also count the number of From (not From:) lines and print out a count at the end. 
This is a good sample output with a few lines removed:
"""

fileName = input("Enter file: ")
extenCheck = fileName.find(".txt")
if extenCheck == -1:
    fileName = fileName + '.txt'
    
openFile = open(fileName, 'r')

lineCounter = 0

for line in openFile :
    words = line.split()
    #print('Debug:', words)
    if line.startswith('From ') == False : 
        continue
    else :
        lineCounter = lineCounter + 1
        print(words[1])

print('There were',lineCounter,'lines in the file with From as the first word')