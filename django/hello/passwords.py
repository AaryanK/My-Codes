import string
import random

upper = string.ascii_uppercase
lower = string.ascii_lowercase
special = string.punctuation
digits = string.digits

a=[]
b=''
a.extend(list(upper))
a.extend(list(lower))
a.extend(list(special))
a.extend(list(digits))

random.shuffle(a)

print(''.join(a[0:9]))



