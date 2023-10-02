# Swap two variables :

x = float(input("Enter a X value : "))
y = float(input("Enter a Y value : "))

temp = 0

temp = x
x = y
y = temp

# another way is :
# x,y = y,x

print("Swap X value is ",x)
print("Swap Y value is ",y)
