# Check leep Year or not :

year = int(input("enter the year : "))

if (year % 400 == 0) and (year % 100 == 0):
    print(year, "its a leep year.")
elif (year % 4 == 0) and (year % 100 != 0):
    print(year, "its a leep year.")
else:
    print(year," its a Not  leep Year.")
