# Write a program input sides of a triangle and check whether triangle is valid or not.
a,b,c=map(int,input("Enter the three sides of the triangle: ").split())
if a+b>c and a+c>b and b+c>a:
    print("Valid triangle")
else:
    print("Invalid triangle")
