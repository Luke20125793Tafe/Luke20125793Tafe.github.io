# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 13:28:37 2024

@author: Geektron

Exercise 1: Write a function called chop that takes a list and modifies it, 
    removing the first and last elements, and returns None. 
Then write a function called middle that takes a list and returns a new list 
    that contains all but the first and last elements.
"""

allNums = [13, 83, 85, 51, 72, 74, 26, 31, 21, 41, 45, 53, 9, 26, 87]
lastInList = len(allNums)-1

def middle():
    midNums = allNums[1:lastInList]
    
    print(midNums)

def chop():
    allNums[0] = None
    allNums[lastInList] = None
    
    print(allNums)

middle()

chop()
