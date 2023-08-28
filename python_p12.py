# Write a program to compute the area of a Trapezium by reading base1, base2 and height
b1=float(input("Enter the value of base1 of trapezium: "))
b2=float(input("Enter the value of base2 of trapezium: "))
h=float(input("Enter the height of trapezium: "))
a=(b1+b2)/2*h
print("Area = {:.2f} square units".format(a))
