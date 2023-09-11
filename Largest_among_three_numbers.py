# Write program to find the largest among three numbers.
a,b,c=map(int,input("Enter three numbers: ").split())
if a>b and a>c:
    print("The largest number is",a)
elif b>a and b>c:
    print("The largest number is",b)
elif c>a and c>b:
    print("The largest number is",c)
else:
    print("The largest number is",a)
