# Write a program to compute the surface area and volume of a cube by taking a side of the cube
s=float(input("Enter the value of a side of cube: "))
sa=6*s*s
v=s*s*s
print("Surface area = {:.2f} square units".format(sa))
print("Volume = {:.2f} cubic units".format(v))
