# Print Left bent Equilateral Triangle pattern with stars.
n=int(input("Enter the number of rows: "))
print()
# Left bent Equilateral Triangle has n+(n-1) rows
for i in range(1,n+(n-1)+1):
    # i^th row has |n-i| leading spaces
    for j in range(1,abs(n-i)+1):
        print("   ",end="")
    # i^th row has n-|n-i| elements and spaces together
    for j in range(1,n-abs(n-i)+1):
        if j%2!=0:
            print("*  ",end="")
        else:
            print("   ",end="")
    print()
