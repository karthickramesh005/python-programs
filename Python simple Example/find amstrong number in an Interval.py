# find amstrong number in an Interval :

lo = int(input("enter the lower limit here : "))
up = int(input("enter the upper limit here : "))

for num in range(lo,up +1):
    order = len(str(num))
    sum =0
    temp = num
    while temp > 0 :
        digit = temp % 10
        sum += digit ** order
        temp //=10
    if num == sum :
        print(num)
