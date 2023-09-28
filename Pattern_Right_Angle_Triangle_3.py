''' Write a program for printing Pattern like a Right angle Triangle (Pattern 3) with stars.
                     *
                    **
Pattern like ==>   ***
                  ****       
'''
n=int(input("Enter the number of Rows: "))
for i in range(1,n+1):
    for j in range(n,1-1,-1):
        if j-i<=0:
            print("*",end="")
        else:
            print(" ",end="")
    print()
