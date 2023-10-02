# print amstrong number using recutsion :

def ams(n):
    if n <= 1:
        return n
    else:
        return (n)+ams(n-1)

n = int(input("Enter the number : "))

if n <0:
    print("please enter a positive number.")
else:
    print(" amstrong number is",ams(n))
