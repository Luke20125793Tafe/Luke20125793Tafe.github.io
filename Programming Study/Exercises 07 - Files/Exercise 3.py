# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 17:31:59 2024

@author: Geektron
"""
import statistics as stats
import sys

def spamCon(fileName) :
    content = []
    
    if fileName == 'na na boo boo.txt' :
        print('NA NA BOO BOO TO YOU - You have been punked!')
        sys.exit()
    else :
        try:
            openFile = open(fileName, 'r')
        except:
            print('File cannot be opened: ', fileName)
            sys.exit()
    
    
    for line in openFile :
            content.append(line.strip())
    
    spamCon = []
    
    for line in content :
        if line.startswith('X-DSPAM-Confidence'):
            colonPos = line.find(':')+1
            spamCon.append(float(line[colonPos:]))
    
    spamAvg = stats.mean(spamCon)
    
    print('Average spam confidence:', spamAvg)
    
    openFile.close()

    

fileName = input('Enter a file name: ')
extenCheck = fileName.find(".txt")
if extenCheck == -1:
    fileName = fileName + '.txt'


spamCon(fileName)