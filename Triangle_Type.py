# Write a program to check whether a triangle is Equilateral, Isosceles or Scalene.
a,b,c=map(int,input("Enter the three sides of a triangle: ").split())
if a+b>c and a+c>b and b+c>a:
    if a==b and a==c and b==c:
        print("Equilateral Triangle")
    elif a==b or a==c or b==c:
        print("Isosceles Triangle")
    else:
        print("Scalene Triangle")
else:
    print("Triangle does not exist!")
