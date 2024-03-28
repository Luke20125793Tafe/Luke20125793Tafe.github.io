"""
Created on Thu Mar 28 17:28:07 2024

@author: Luke W

Exercise 2: This program counts the distribution of the hour of the day for each of the messages. 
You can pull the hour from the “From” line by finding the time string and then splitting that string
     into parts using the colon character. Once you have accumulated the counts for each hour, 
     print out the counts, one per line
"""

hourSent = dict()


fileName = input('Enter a file name: ')

#QOL to check for .txt extension and add if missing
if fileName.find(".txt") == -1:
    fileName = fileName + '.txt'

openFile = open(fileName)

for line in openFile :
    words = line.split()
    #print('Debug:', words)
    if len(words) < 2 or words[0] != 'From' : 
        continue
    else:
        #print(words)
        for word in words:
            if word.find(':') == -1:
                continue
            else:
                #print(word)
                if word[0:2] not in hourSent:
                    hourSent[word[0:2]] = 1
                else:
                    hourSent[word[0:2]] = hourSent[word[0:2]] + 1

hourCount = list()
for key, val in list(hourSent.items()):
    hourCount.append((key, val))
    
hourCount.sort(reverse=False)

for key, val in hourCount:
    print(key, val)
