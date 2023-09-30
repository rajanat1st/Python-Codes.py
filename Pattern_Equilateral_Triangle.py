# Print Equilateral Triangle pattern with stars.
n=int(input("Enter the number of Rows: "))
for i in range(1,n+1):
    # i^th row has (n-i) leading spaces
    for j in range(1,n-i+1):
        print(" ",end="")
    # i^th row has i elements
    for j in range(1,i+1):
        print("* ",end="")
    print()
