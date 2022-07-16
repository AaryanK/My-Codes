import string
import random

def strong(character):
    alphabets = string.ascii_letters #It gives all the alphabets from A-Z and a-z
    digits = string.digits #It gives numbers from 0-9
    special = string.punctuation #It gives special characters.

    raw_pass = list(alphabets+digits+special)

    random.shuffle(raw_pass)

    password = ""
    for i in raw_pass:
        password+=i #same as password = password+i
    final_pass = password[:character]
    return final_pass

