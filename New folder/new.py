a = [1,9,6,7,86,8,0]


swaps = True
while swaps == True:
    swaps = False
    for i in range(len(a)-1):
        if a[i]>a[i+1]:
            temp = a[i]
            a[i] = a[i+1]
            a[i+1] = temp
            swaps = True
        

        

print(a)