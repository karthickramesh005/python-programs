# Check number Odd or Even :

def check(num):
    if num % 2 == 0:
        print(num, " is the Even number.")
    elif num % 2 == 1:
        print(num, " is the Odd number.")
    else :
        print(num," was zero")

num = int(input("enter the number : "))
check(num)
