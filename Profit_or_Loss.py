''' Write a program to calculate profit or loss on a transaction. Given that, the cost price and selling price of an item
respectively.
Note: If cost price and selling price are equal then print "No profit No loss". '''
c=int(input("Enter the cost price: "))
s=int(input("Enter the selling price: "))
if c<s:
    print("\nProfit")
elif c>s:
    print("\nLoss")
else:
    print("\nNo Profit No Loss")
