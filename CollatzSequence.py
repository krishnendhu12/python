name=input("Krishnendhu: ")
USN=input("1AY24BT023: ")
def collatz(n):
    if(n==1):
        return
    elif(n%2==0):
         num1=n//2
         print(num1)
    else:
        num2=n*3+1
        print(num2)
collatz(3)  
