# Print Right bent Equilateral Triangle pattern with stars.
n=int(input("Enter the number of rows: "))
print()
# Right bent Equilateral Triangle has n+(n-1) rows
for i in range(1,n+(n-1)+1):
    # i^th row has n-|n-i| elements and spaces together
    for j in range(1,n-abs(n-i)+1):
        # For i, Odd row starts with element and Even row starts with space
        if i%2!=0:
            if j%2!=0:
                print("*  ",end="")
            else:
                print("   ",end="")
        else:
            if j%2!=0:
                print("   ",end="")
            else:
                print("*  ",end="")
    print()
