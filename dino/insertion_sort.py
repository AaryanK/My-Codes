def insertion_sort(a):
    for i in range(1,len(a)):
        j = i
        while a[j-1]>a[j] and j>0:
            a[j-1],a[j] = a[j],a[j-1]
            j-=1


a = [47,6,54,17,93,28]
print(a)
insertion_sort(a)
print(a)

