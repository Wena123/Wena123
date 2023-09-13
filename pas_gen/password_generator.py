import string
import random

def generate_password(min_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special_characters = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special_characters

    pwd = ''
    meets_cri = False
    has_num = False
    has_special = False

    while not meets_cri or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_num = True
        elif new_char in special_characters:
            has_special = True

        meets_cri = True
        if numbers:
            meets_cri = has_num
        if special_characters:
            meets_cri = meets_cri and has_special

    return pwd

min_length = int(input("enter the min lenght: "))
pwd = generate_password(10)
print(pwd)