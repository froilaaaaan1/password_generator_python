"""" this module is reponsible for generating a random password based on the length given """
import random
import string
import sys
import os

LETTERS = string.ascii_letters
NUMBERS = string.digits
PUNCTUATION = string.punctuation

print("This tool will generate random characters for password. User will specify their requirements according to "
      "their needs")


def initiator():
    """ this function is the initiator of generator it'll handle conditionals """
    user_input = ""
    try:
        user_input = int(input("How many chars do you want to generate? "))
    except ValueError:
        os.system('cls')
        print("Must enter a valid number")
        initiator()

    if user_input < 8:
        os.system('cls')
        print("As per general rule password length must be greater than 8, try again.")
        initiator()

    has_nums = input('Include numbers? Y/N ')
    has_punc = input('Include punctuations? Y/N ')

    nums = True if has_nums.lower() == 'y' else False
    punc = True if has_punc.lower() == 'y' else False

    pass_gen(user_input, punc, nums)


def pass_gen(length: int, punctuated: bool, nums: bool):
    """ this module is responsible for generating the password itself """
    if punctuated is True and nums is True:
        generated_password = random.choices(
            LETTERS + NUMBERS + PUNCTUATION, k=length)
        conv(generated_password)
    if punctuated is True and nums is False:
        generated_password = random.choices(LETTERS + PUNCTUATION, k=length)
        conv(generated_password)
    if punctuated is False and nums is True:
        generated_password = random.choices(LETTERS + NUMBERS, k=length)
        conv(generated_password)
    if punctuated is False and nums is False:
        generated_password = random.choices(LETTERS, k=length)
        conv(generated_password)


def conv(letter_arr):
    """ this will loop over the array of letters on the given input """
    final_password = ''
    for letter in letter_arr:
        final_password += letter
    print(final_password)
    again = input('Regenerate? Y/N: ')
    if again.lower() == 'y':
        os.system('cls')
        initiator()
    sys.exit(0)


initiator()
