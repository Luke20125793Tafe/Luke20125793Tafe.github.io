##############################################################
#
# Caesar cipher program
#
# File:      ICTPRG302/CLASSWORK/Caesar-Cipher.py
# Author:    Ingrid Aldum  (ingrid.aldum@nmtafe.wa.edu.au)
# Copyright: Copyright 2022, Ingrid Aldum
#
##############################################################
#
def welcome():
    '''Print welcome message using person's name'''
    print ("Welcome to Caesar cipher program")
    name = input("What is your name? ")
    print(name, "hope you enjoy encrypting and decrypting words.")
    return(name)

def encrypt(letter, shift):
    '''encrypt the message'''
    if letter.isalpha():
        answer = chr(ord(letter)+shift)
    else:
        answer = letter
    return(answer)


#main program starts here
answer = ""
username = welcome()
word = input("Please give a word to encrypt ")
shift = input("Shift with how many? ")

try:
    shift = int(shift)
    for letter in word:
        answer = answer + encrypt(letter, shift)
except:
    print("Shift is not a number, cannot perform this action")
    answer = answer + letter
print("Word:", word, "\nCaesar cipher:", answer)



