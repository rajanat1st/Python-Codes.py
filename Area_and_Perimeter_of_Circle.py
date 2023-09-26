# Write program to calculate the area and perimeter of a circle by reading the radius.
from math import pi
r=float(input("Enter the radius of the circle: "))
a=pi*r*r
p=2*pi*r
print("Area = {:.2f}  square units\nPerimeter = {:.2f} units".format(a,p))
