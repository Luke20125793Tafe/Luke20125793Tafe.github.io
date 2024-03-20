# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 17:31:59 2024

@author: Geektron
"""
def spamCon(fileName) :
   
    try:
        openFile = open(fileName, 'r')
    except:
        print('File cannot be opened: ', fileName)
            
    spamCon = []
    spamTotal = 0
    
    for line in openFile :
        if not line.startswith('X-DSPAM-Confidence'):
            continue
        else :
            colonPos = line.find(':')+1
            justNumber = float(line[colonPos:])
            spamCon.append(justNumber)
            spamTotal = spamTotal + justNumber
                        
    spamCount = len(spamCon)
    spamAvg = spamTotal / spamCount  
        
    print('Average spam confidence:', spamAvg)
    
    openFile.close()

fileName = input('Enter a file name: ')
extenCheck = fileName.find(".txt")
if extenCheck == -1:
    fileName = fileName + '.txt'


spamCon(fileName)