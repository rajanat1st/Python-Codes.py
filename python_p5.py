# Write a program to calculate the distance between the two points (x1,x2) and (y1,y2).
import math
x1,y1=map(int,input("Enter the value of x1 and y1: ").split())
x2,y2=map(int,input("Enter the value of x2 and y2: ").split())
d=math.sqrt(((x2-x1)**2)+((y2-y1)**2))
print("The distance between the two points is {:.2f} units".format(d))
