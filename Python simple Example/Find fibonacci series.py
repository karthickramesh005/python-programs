# Find fibonacci series :

a = 0
b = 1

n = int(input("enter a number to obtain fibonacci sequence : "))

if n == 1:
    print(a)
else:
    print(a)
    print(b)
    for i in range(2,n+1):
        c = a + b
        a = b
        b = c
        print(c)
