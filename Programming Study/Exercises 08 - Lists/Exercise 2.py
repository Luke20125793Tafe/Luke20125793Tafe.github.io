# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 13:42:12 2024

@author: Geektron

Exercise 2: Figure out which line of the above program is still not properly guarded. 
See if you can construct a text file which causes the program to fail and then modify 
    the program so that the line is properly guarded and test it to make sure it handles your new text file.
"""
fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    words = line.split()
    #print('Debug:', words)
    if len(words) == 0 : continue
    if words[0] != 'From' : continue
    print(words[2])
    
"""
Apparently the unguarded portion is:
    "he problem is if the line has less than 3 words it will crash at the print(words[2]) command."
I cannot seem to replicate this at all: solition for this is the following

fhand = open('8.2 Crasher.txt')
count = 0
for line in fhand:
    words = line.split()
    print('Debug:', words)
    if len(words) < 2 : continue
    if words[0] != 'From' : continue
    print(words[2])

the "if len(words) < 2 : continue" catches any less than 3 words in length, which makes the line
    "if len(words) == 0 : continue" reduntant so it is replaced with the new one.

"""