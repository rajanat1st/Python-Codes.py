# Print Inverted Equilateral Triangle pattern with stars.
n=int(input("Enter the number of Rows: "))
for i in range(1,n+1):
    for j in range(1,i):
        print(" ",end="")
    for j in range(1,n-i+2):
        print("* ",end="")
    print()
