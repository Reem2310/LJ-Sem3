a=int(input("Enter the number of first base : "))
b=int(input("Enter the number of Second base : "))
h=int(input("Enter the number of the height : "))
if a>0 or b>0 or h>0:
    area_trapzoid=((a+b)/2)*h
    print(f"The Area of the trapzoid is : {area_trapzoid:.2f}")
else:
    print("Invalid Value")