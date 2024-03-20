# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 16:57:51 2024

@author: Geektron

Exercise 2: Write a program that categorizes each mail message by which day of the 
    week the commit was done. 
To do this look for lines that start with “From”, then look for the third word 
    and keep a running count of each of the days of the week. 
At the end of the program print out the contents of your dictionary (order does not matter).
"""

dayCount = dict()

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
        dayWeek = words[2]
        if dayWeek not in dayCount:
            dayCount[dayWeek] = 1
        else:
            dayCount[dayWeek] = dayCount[dayWeek] + 1

print(dayCount)