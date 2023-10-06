# Write a Python program to multiply two floating-point numbers.
a,b=map(float,input("Enter two floating-point numbers (with 2 decimal numbers): ").split())
c=a*b
print("{:.2f} X {:.2f} = {:.2f}".format(a,b,c))
