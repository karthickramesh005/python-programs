# Check amstrong number :

num = int(input("enter a number : "))

sum = 0
temp = num

while temp > 0:
    digit = temp % 10
    cube = digit ** 3
    sum += cube
    temp //=10

if sum == num:
    print("its a amstrong number.")
else :
    print("Its not amstrong number.")
