# Check Prime number or not :

num = int(input("Enter the  number :  "))

if num == 1 :
    print(num," its Not Prime number.")
elif num > 1:
    for i in range (2,num):
        if(num % i)== 0:
            print(num," its Not Prime number.")
            break
    else:
        print(num," its  Prime number.")
