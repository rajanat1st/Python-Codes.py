# Print Inverted Mirrored Right angle Triangle pattern with stars.
n=int(input("Enter the number of Rows: "))
for i in range(1,n+1):
    # i^th row has (i-1) leading spaces
    for j in range(1,i):
        print("  ",end="")
    # i^th row has (n-i+1) elements
    for j in range(1,n-i+2):
        print("* ",end="")
    print()
