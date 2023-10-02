# print prime number on interval :

lo = int(input("enter the starting number : "))
up = int(input("enter the end number : "))

for num in range(lo,up+1):
    if num > 1:
        for i in range(2,num):
            if(num % i) == 0:
                break
        else:
            print(num)
