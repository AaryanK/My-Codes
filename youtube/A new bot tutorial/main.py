from engine.login import login

password = input("Enter your master password here : ")
log = login(password)
if log =='12345':
    print("Hello Aaryan!")

else:
    print(log)
