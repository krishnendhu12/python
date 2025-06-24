import random
name=input("Krishnendhu: ")
USN=input("1AY24BT023: ")
target=random.randint(0,20)
for i in range(20):
    choice=int(input("guess a number from 1 to 20:"))
    if(choice==target):
        print("you have guessed right number")
        print("you have guessed numbered in" ,i,"attempt")
        break
    elif(choice<target):
        print("low guess")
    else:
        print("high guess")
