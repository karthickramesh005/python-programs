# Find sum of natural numbers :

num = int(input("Enter a value : "))

sum = 0

if num < 0:
    print("Please enter a positive number.")
else:
    while num > 0:
        sum += num
        num-=1
    print(sum)
