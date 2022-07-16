import pandas as pd
import csv






def add_data(fname,lname,age):
    with open('data.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',',)
        writer.writerow([f'{fname.lower()}']+ [f'{lname.lower()}']+[f'{age}'])
def read(fname):
    csv_file = open("data.csv",'r+')
    csv_file = csv.reader(csv_file)
    next(csv_file)
    for name in csv_file:
        if fname.lower()==name[0]:
            print("Record found")
            print(f"Details\nFirst Name:{fname}\nLast name:{name[1][name[0].index(fname)]}\nAge:{name[2][name[0].index(fname)]}")
    


a = input("Enter the first name")
b = input("Enter the last name")
c = input("Enter the last age")

add_data(a,b,c)

'''z = input("ENter a first name")
read(z)'''