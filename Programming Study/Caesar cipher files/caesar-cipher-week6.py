##############################################################
#
# Caesar cipher program
#
# File:      ../caesar-cipher-week6.py
# Author:    TAFE
# Copyright: Copyright 2023
#
##############################################################
def welcome():
    '''Print welcome message using person's name'''
    print ("Welcome to Caesar cipher program")
    name = input("What is your name? ")
    print(name, "hope you enjoy encrypting and decrypting words.")
    return(name)

def user_input():
    print("\n###############################################################")
    print("# Enter a string containing the following:                    #")
    print("# First character e for encrypt, d for decrypt                #")
    print("# Next three characters:                                      #")
    print("# number of characters to encrypt with or                     #")
    print("# number of characters original message was encrypted with    #")
    print("###############################################################")
    encrypt_decrypt_string = input(">>> ")
    print("\n###############################################################")
    return(encrypt_decrypt_string)


def encrypt(shift, word):
    "encrypt the message"
    message = ""
    for letter in word:
        message = message +chr(ord(letter)+shift)
    return(message)


def validate_input(pre_fix):
    DECRYPT_SWITCH = -1
    try:
        pre_fix = encrypt_decrypt_string[:4].lower().strip()
        shift = int(pre_fix[1:])
    except:
        print("Shift is not a number, could not encrypt / decrypt the message.")
        print("Program is stopping, press enter")
        quit()

    if pre_fix[0] == "d":
        shift = shift * DECRYPT_SWITCH
    elif pre_fix[0] != "e":
        print("Invalid encrypt / decrypt value")
        print("Program is stopping, press enter")
        quit()
    return shift

def encrypt(shift, line):
    '''encrypt the message'''
    message = ""
    for letter in line:
        message = message + chr(ord(letter) + shift)
    return (message)


#main program starts here
encrypt_decrypt_string = user_input()
shift = validate_input(encrypt_decrypt_string)
print('The encrypted word is:', encrypt(shift, encrypt_decrypt_string[4:]))
