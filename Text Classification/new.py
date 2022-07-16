
# A = [10,9,7,1,2,3]
# print(A)
# count = 1
# while True:
#     swapped = False
#     for i in range(len(A)-1):
#         if A[i] > A[i+1]:
#             swapped = True
#             A[i], A[i+1] = A[i+1], A[i]
#     print(f"Pass number {count}:{A}")
#     count+=1
#     if swapped == False:
#         break

def CountVowels(string):
    string = string.lower()
    count = 0
    CharCount = []
    for i in range(6):
        CharCount.append(0)
    print(CharCount)
    for i in string:
        if i == "a":
            CharCount[0]+=1
        elif i == "e":
            CharCount[1]+=1
        elif i == "i":
            CharCount[2]+=1
        elif i == "o":
            CharCount[3]+=1
        elif i == "u":
            CharCount[4]+=1
        elif i >"a" and i<"z":
            CharCount[5]+=1
    print(CharCount)
    return count
CountVowels("Aavash")