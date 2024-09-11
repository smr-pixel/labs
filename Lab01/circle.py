radius = input("Enter the radius of a circle.")
radius = float(radius)
import math
perimeter = 2 * radius * math.pi
area = math.pi * radius**2
round_area = round(area, 2)
round_perimeter = round(perimeter, 2)
round_radius = round(radius, 2)
area = str(round_area)
perimeter = str(round_perimeter)
radius = str(round_radius)
print("The area of a circle with radius " + radius + " has an area of " + area + " and a perimeter of " + perimeter)