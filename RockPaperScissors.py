import random
name=input("Krishnendhu: ")
USN=input("Enter your 1AY24BT023: ")
while True:
    user_choice=input("Enter your move : (a)rock (b)paper (c)seissor (d)quit ")
    if user_choice == "d":
        break
    choice=["a","b","c"]
    if user_choice not in choice:
        print("Invalid option try again")
        continue
    computer_choice=random.choice(choice)
    
    if user_choice==computer_choice:
        print("Its tie")
    elif(user_choice=="a" and computer_choice=="c")or \
        (user_choice=="b" and computer_choice=="a")or \
        (user_choice=="c" and computer_choice=="b"):
         print("you won")
    else:
        print("you lost")
