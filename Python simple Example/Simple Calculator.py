# Simple Calculator :

def add(x,y):
    sum = x + y
    return sum

def sub(x,y):
    sum = x - y
    return sum
def div(x,y):
    sum = x / y
    return sum

def mul(x,y):
    sum = x * y
    return sum

def mod(x,y):
    sum = x % y
    return sum
    
x = float(input("Enter a first value : "))
y = float(input("Enter a second value : "))

op =str(input("Enter the operation : "))

if op == '+':
    print("Your answer is : ",add(x,y))
elif op =='-':
    print("Your answer is : ",sub(x,y))
elif op == '*':
    print("Your answer is : ",mul(x,y))
elif op == '/':
    print("Your answer is : ",div(x,y))
elif op == '%':
    print("Your answer is : ",mod(x,y))
else:
    print("Please! enter a currect operation.")
    
