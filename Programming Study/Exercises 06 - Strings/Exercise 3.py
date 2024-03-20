# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 16:03:53 2024

@author: Geektron
"""

def count(word) :
    count = 0
    for letter in word:
        if letter == 'a' or letter =='A':
            count = count + 1
    print(count)
        
theWord = input("Please enter a word: ")

count(theWord)