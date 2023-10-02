# find average of N Numbers :

num = int(input("how many number : "))
total = 0

for i in range (num):
    numbers = int(input("enter the number : "))
    total += numbers

avg = total/ num
print("average : ",avg)
