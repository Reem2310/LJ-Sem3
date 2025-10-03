import math
radius = float(input("Enter the radius of the cylinder: "))
height = float(input("Enter the height of the cylinder: "))

if radius < 0 or height < 0:
        print("Invalid input. The radius and height cannot be negative.")
else:
        volume = math.pi * (radius ** 2) * height
        surface_area = (2 * math.pi * radius * height) + (2 * math.pi * (radius ** 2))
        print(f"\nThe volume of the cylinder is: {volume:.2f}")
        print(f"The total surface area of the cylinder is: {surface_area:.2f}")



