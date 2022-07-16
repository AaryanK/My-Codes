import random
number = list('123456789')
indexes=list('123')

final_number=''
for i in range(int(random.choice(indexes))):
    final_number+=random.choice(number)

guess = 0
times = 0
print("Enter QUIT to exit")
while guess!=final_number:
    if times >0:
        print("Wrong guess")
    guess = input("Enter your guess : ")
    if guess=="QUIT":
        break
    else:
        guess=int(guess)
    
    times+=1

if guess==final_number:
    print("Congratulations you won")
print(f"The number was {final_number}")



