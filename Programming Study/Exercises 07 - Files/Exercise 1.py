# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 17:31:59 2024

@author: Geektron
"""

def shout(fileName) :
    openFile = open(fileName, 'r')
    content = openFile.read()

    print(content.upper())

fileName = input('Enter a file name: ')
extenCheck = fileName.find(".txt")
if extenCheck == -1:
    fileName = fileName + '.txt'


shout(fileName)