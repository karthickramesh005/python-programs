# find HCF or GCD :

def HCF(x,y):
    if  x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1,smaller + 1):
        if ((x % i == 0) and (y % i == 0)):
            hcf = i
    return hcf

x = int(input("Enter a first value of find HCF : "))
y = int(input("Enter a second value of find HCF : "))

print("The HCF of given two number is ",HCF(x,y))
