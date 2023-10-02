# Find factorial of N :

n = int(input("enter the number : "))


fact = 1

if (n < 0):
    print("sorry! factorial of 0 is does not exit")
elif (n == 0):
    print("factoral of 0 is ", 1)
if n > 1:
    for i in range(1,n+1):
        fact *= i
print("factorial of ",n," is ",fact,".")
        
