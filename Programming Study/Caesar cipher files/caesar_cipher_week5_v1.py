##############################################################
#
# Caesar cipher program
#
# File:      caesar_cipher_week5.py
# Author:    TAFE
# Copyright: 2023
#
##############################################################

def welcome():
    '''Prints a welcome message using a person's name'''
    print("Welcome to Caesar cipher program")
    name = input("What is your name? ")
    print(name, "hope you enjoy encrypting and decrypting words.")
    return name


def encrypt(shift, word):
    '''encrypt the message'''
    message = ""
    for letter in word:
        message = message + chr(ord(letter)+shift)
    return message


def decrypt(shift, word):
    '''decrypt the message'''
    return encrypt(-shift, word)  # call encrypt function with the opposite shift


def get_message_from_input():
    print("\n###############################")
    print("Enter a string containing the following:")
    print("First character e for encrypt, d for decrypt")
    print("Next three characters:")
    print("number of characters to encrypt with or")
    print("number of characters message was encrypted with originally")
    print("number may be a negative number")
    print("\n###############################")
    encrypt_decrypt_message = input(">>> ")
    print("\n###############################")
    return encrypt_decrypt_message


def main():
    '''Main program'''
    welcome()
    encrypt_decrypt_message = get_message_from_input()
    prefix = encrypt_decrypt_message[:4].lower()
    try:
        shift = int(prefix[1:].strip())
    except ValueError:
        print(
            f"Shift {prefix[1:]} is not a number; cannot encrypt or decrypt.")
    else:
        if prefix.startswith('e'):
            print('The encrypted word is:', encrypt(
                shift, encrypt_decrypt_message[4:]))
        elif prefix.startswith('d'):
            print('The decrypted word is:', decrypt(
                shift, encrypt_decrypt_message[4:]))
        else:
            print("Cannot encrypt or decrypt due to an invalid input.")


main()  # start the program
