# Find factors of number:

num = int(input("enter the number in here : "))

for i in range(1,num+1):
    if num % i == 0 :
        print(i)
