b=int(input("Enter the Value of the base : "))
h=int(input("Enter the Value of the Height : "))
if b>0 or h>0:
    area=0.5*b*h
    print(f"The triangle of base {b} and height {h} of the area is {area}")
else:
    print("Invalid input. Please enter numeric values for base and height.")