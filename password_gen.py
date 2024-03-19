import random
import string

def password_generator(min_length, number=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if number:
        characters += digits
    if special_characters:
        characters += special

    password = ''
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(password) < min_length:
        new_char = random.choice(characters)
        password += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

        meets_criteria = True
        if number:
            meets_criteria = has_number
        if special_characters:
            meets_criteria = meets_criteria and has_special

    return password

min_length = int(input('Enter the minimum length: '))
has_number = input('Do you want to have numbers? (y/n) ').lower() == 'y'
has_special = input('Do you want to have special characters? (y/n) ').lower() == 'y'
password = password_generator(min_length, has_number, has_special)
print(password)