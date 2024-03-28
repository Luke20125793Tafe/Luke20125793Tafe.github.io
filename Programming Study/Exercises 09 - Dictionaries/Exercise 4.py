# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 16:57:51 2024

@author: Geektron

Add code to the above program (from Exercise 3) to figure out who has the most messages in the file. 
After all the data has been read and the dictionary has been created, look through the dictionary 
    using a maximum loop (see Chapter 5: Maximum and minimum loops) to find who has the most messages 
    and print how many messages the person has.
"""

emailHistorgram = dict()
mostFromCount = 0
mostFrom = None
leastFromCount = 0
leastFrom = None

fileName = input('Enter a file name: ')
extenCheck = fileName.find(".txt")
if extenCheck == -1:
    fileName = fileName + '.txt'
    
openFile = open(fileName)

for line in openFile :
    words = line.split()
    #print('Debug:', words)
    if len(words) < 2 or words[0] != 'From ' : 
        continue
    else:
        emailFrom = words[1]
        if emailFrom not in emailHistorgram:
            emailHistorgram[emailFrom] = 1
        else:
            emailHistorgram[emailFrom] = emailHistorgram[emailFrom] + 1
            

for entry in emailHistorgram :
    email = entry
    emailCount = emailHistorgram[entry]
    #print(email, emailCount)
    if emailCount > mostFromCount :
        mostFromCount = emailCount
        emailCount = str(emailCount)
        mostFrom = email + " " + emailCount
    elif leastFromCount == 0 or emailCount > leastFromCount :
        leastFromCount = emailCount
        emailCount = str(emailCount)
        leastFrom = email + " " + emailCount

print('Most emails from:',mostFrom)
print('Least emails from:',leastFrom)