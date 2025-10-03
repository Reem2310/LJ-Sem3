import math
r=int(input("Enter the Radius of the circle is : "))
if r>0:
    area=math.pi*(r**2)
    print(f"The Area of the Circle is : {area}")
else:
    print("Please Enter a Correct Value ")