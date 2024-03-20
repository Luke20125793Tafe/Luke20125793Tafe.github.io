# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 15:33:09 2024

@author: Geektron

Exercise 6:

Rewrite the program (from Exercise 5) that prompts the user for a list of numbers 
    and prints out the maximum and minimum of the numbers at the end when the user enters “done”. 
Write the program to store the numbers the user enters in a list and use the max() and min() functions
    to compute the maximum and minimum numbers after the loop completes.
"""

newNumber = None
listNumbers = list()
keepGoing = int()

while keepGoing < 10 :
    newNumber = input("Enter a number: ")
    
    if newNumber == "done" or newNumber == "Done" :
        break
    else :
        try :
            newNumber = int(newNumber)
            listNumbers.append(newNumber)
        except :
            print("invalid input")
    keepGoing = keepGoing + 1
            
print('Maximum: ', max(listNumbers))
print('Minimum: ', min(listNumbers))



            