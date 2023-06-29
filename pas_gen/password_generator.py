import string
import random

def generate_password(min_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special_characters = string.punctuation

    print(letters, digits, special_characters)