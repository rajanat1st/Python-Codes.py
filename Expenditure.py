''' Akshat has X rupees to spend in the current month. His daily expenditure is Y rupees, ie., he spends Y rupees each day.
Given that the current month has 30 days, find out if Akshat has enough money to meet his daily expenditures for this month.(X and Y are
taken from the console) '''

x=int(input("Enter the amount Akshat is having now(X): "))
y=int(input("Enter the amount Akshat spends each day(Y): "))
if y*30<=x:
    print("\nAkshat has enough money")
else:
    print("\nAkshat does not have enough money")
