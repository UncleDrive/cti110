# Zavier Gaines
# June 23 2025
# P2LAB1
# we are getting the circomference diameter and area of a circle using the formulas that we are given

import math

radius = float(input("What is the radius of the circle? "))


  
diameter = 2 * radius

circomference = 2 * math.pi * radius
area = math.pi * (radius ** 2)

print()
print("The diameter of the circle is", format(diameter, ".1f"))
print()
print("The circomference of the circle is", format(circomference, ".2f"))
print()
print("The area of the circle is", format(area, ".3f"))
