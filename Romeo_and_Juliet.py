'''Romeo has X 5 rupee coins and Y 10 rupee coins. Romeo goes to a shop to buy chocolates for Juliet where each chocolate costs
Z rupees. Find tne maximum number of chocolates that Romeo can buy for Juliet (Take X, Y and Z from the console).'''
x=int(input("Enter the value of X: "))
y=int(input("Enter the value of Y: "))
z=int(input("Enter the value of Z: "))
c=((x*5)+(y*10))//z
print("The maximum chocolates Romeo can buy =",c)
