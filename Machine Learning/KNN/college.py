a= input ("Enter first number : ")
a2=input ("Enter second number : ")
a3=input ("Enter third number : ")

list = [a,a2,a3]
greatest = list[0]

for i in list:
    if i > greatest:
        greatest = i

print(f"Greatest number is {greatest}")
