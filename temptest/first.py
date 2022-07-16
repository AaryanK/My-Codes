def table(number,times):
    for i in range(times):
        print(f"{number}X{i}={number*i}")

a = int(input("enter a number : "))
b = int(input("how many times : "))+1

table(a,b)