##############################################################
#
# Caesar cipher program
#
# File:      caesar-cipher-week7.py
# Author:    TAFE
# Copyright: Copyright 2023
#
##############################################################
def welcome():
    '''Print welcome message using person's name'''
    print ("Welcome to Caesar cipher program")
    name = input("What is your name? ")
    print(name, "hope you enjoy encrypting and decrypting words.")
    return name


def get_input_file_name_input():
    '''Obtain the filename of the file that needs to be encrypted / decrupted'''
    while True:
        print("\n###########################################################")
        print("# Please enter the filename of file to encrypt / decrypt: #")
        print("###########################################################")
        file_name = input()
        try:
            encrypt_file_handle = open(file_name, "r")
            return encrypt_file_handle
        except:
            print("\nThe file does not exist")
            again = input("Press Q to quit or try again")
        if again.upper() == "Q":
            quit()

def get_output_file_name():
    '''Determine the name of the file to write the encrypt / decrupt data to'''
    while True:
        print("\n#####################################################################")
        print("# Please enter the filename of file to write decrypted / encrypted: #")  # ")
        print("#####################################################################")
        file_name = input()
        if file_name == '':
            print("No filename was entered. Please retry")
        else:
            output_file_handle = open(file_name, "w")
            return output_file_handle, file_name

def validate_input_file(pre_fix):
    '''Check if the file's first line has info regarding encrypting and decrypting'''
    pre_fix = pre_fix.lower()
    try:
        shift = int(pre_fix[1:].strip())
    except ValueError:
        print(
            f"Shift {prefix[1:]} is not a number; cannot encrypt or decrypt.")
        input("The program is stopping. Press enter.")
        quit()
    else:
        if pre_fix[0] in "ed":
            encrypt_indicator = pre_fix[0]
            return encrypt_indicator, shift
        else:
            print("Cannot encrypt or decrypt due to an invalid input.")
            input("The program is stopping. Press enter.")
            quit()


def encrypt(shift, line):
    '''encrypt the message'''
    message = ""
    for letter in line:
        message = message + chr(ord(letter)+shift)
    return message

def decrypt(shift, line):
    '''decrypt the message'''
    return encrypt(-shift, line)  # call encrypt function with the opposite shift

def main():
    first_line = True
    name = welcome()
    encrypt_file_handle = get_input_file_name_input()

    for line in encrypt_file_handle:
        if first_line is True:
            first_line = False
            encrypt_indicator, shift = validate_input_file(line)
            output_file, output_file_name = get_output_file_name()

            if encrypt_indicator == 'e':
                output_file.write("d" + str(shift) + "\n")
            elif encrypt_indicator == 'd':
                output_file.write("e" + str(shift) + "\n")
            continue

        if encrypt_indicator == "e":
            message = encrypt(shift, line.strip())
        else:
            message = decrypt(shift, line.strip())

        output_file.write(message + "\n")
    output_file.close()
    print(f"\n{name} your file: {output_file_name} was successfully created.")


main()  # start the program