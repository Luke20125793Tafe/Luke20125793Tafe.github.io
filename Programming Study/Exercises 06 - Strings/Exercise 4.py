# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 16:19:08 2024

@author: Geektron
"""

fruit = 'banana'
startPos = 0
numberA = 0

while startPos < len(fruit) :
    findA = fruit.find('a', startPos)
    startPos = findA + 1
    numberA = numberA + 1

print('number of "a"s:', numberA)