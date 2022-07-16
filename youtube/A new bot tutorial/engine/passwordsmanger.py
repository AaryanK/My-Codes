import string
import random


def generate_strong_password(length):
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    special_characters = string.punctuation
    numbers = string.digits

    raw_password_list = []
    raw_password = ''

    raw_password_list.extend(list(upper))
    raw_password_list.extend(list(lower))
    raw_password_list.extend(list(special_characters))
    raw_password_list.extend(list(numbers))
    random.shuffle(raw_password_list)

    password = raw_password.join(raw_password_list[0:int(length)])
    return password
    
    
