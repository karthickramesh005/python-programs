# Display Fibonacci sequense using Recursion :

def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n-1)+fibo(n-2)

n = int(input("Enter the find Fibonascci number : "))
if n <= 0:
    print("please enter the positive number.")
else:
    print("Fibonacci Sequense")
    for i in range(n):
        print(fibo(i))
