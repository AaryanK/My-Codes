from threading import Thread

def myfunc():
    while True:
        print('Aaryan')

def mfunc():
    while True:
        print('Prapti is a bitch')


t1 = Thread(target=myfunc)
t2 = Thread(target=mfunc)
t1.start()
t2.start()
