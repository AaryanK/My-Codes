import random

def generate_otp():
    numbers = '0123456789'
    otp_list = []
    numbers=list(numbers)
    random.shuffle(numbers)
    otp_list.extend(numbers)
    otp = "".join(otp_list[:6])
    return otp 

def send_otp(email):
    
