# Find Largest number among the three :

a = float(input("Enter the first number : "))
b = float(input("Enter the Second number : "))
c = float(input("Enter the Third number : "))

if (a > b) and (a > c):
    print(a, "is Greater then ",b, "and ",c,".")
elif (b > a) and (b > c):
    print(b, "is Greater then ",a, "and ",c,".")
else:
    print(c, "is Greater then ",a, "and ",b,".")
