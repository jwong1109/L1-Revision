""" Area and Volume of Sphere
Created by Joseph Wong
7/02/2022
"""
import math

# Input radius of the sphere
radius = float(input("Enter the radius of the sphere: "))
# Calculate volume based on the formula, rounded to 2 decimal places
volume = round (4/3 * math.pi * radius * radius * radius, 2)
# Calculate surface area based on the formula, rounded to 2 decimal places
surface_area = round(4 * math.pi * radius * radius, 2)

# Output Volume and Surface Area based on the radius of the sphere
print("The volume of the sphere is ", volume, "cubic centimetres.")
print("The surface area of the sphere is ", surface_area,
      "square centimetres.")
