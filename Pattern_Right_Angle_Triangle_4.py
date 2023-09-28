''' Write a program for printing Pattern like a Right angle Triangle (Pattern 4) with stars.
                  ****
                   ***
Pattern like ==>    **
                     *       
'''
n=int(input("Enter the number of Rows: "))
for i in range(n,1-1,-1):
    for j in range(n,1-1,-1):
        if i-j>=0:
            print("*",end="")
        else:
            print(" ",end="")
    print()

