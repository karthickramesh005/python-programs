# print factorial number using recutsion :

def fact(n):
    if n == 1:
        return 1
    else:
        return (n)* fact(n-1)

n = int(input("Enter the number : "))

if n <=0:
    print("factorial of number less then 1 does not exists.")
else:
    print(" Factoral of number is",fact(n))
