''' Write a program to calculate and print the Electricity bill of a given customer. Units consumed by the user should be taken from the 
keyboard and display the total amount to be paid by the customer.
The charges are as follows:
Unit                                    Charge/Unit

upto 199                                1.20/-
200 and above but less than 400         1.50/-
400 and above but less than 600         1.80/-
600 and above                           2.00/-

If the bill exceeds Rs.400 then a surcharge of 15% will be charged.
If the bill is less than Rs.400 then a minimum surcharge amount should be Rs.100. '''

u=int(input("Enter the units consumed: "))
if u<200:
    a=u*1.2
elif u<400:
    a=(199*1.2)+(u-199)*1.5
elif u<600:
    a=(199*1.2)+(200*1.5)+(u-399)*1.8
elif u>=600:
    a=(199*1.2)+(200*1.5)+(200*1.8)+(u-599)*2

if a>400:
    ta=a+(a/100)*15
else:
    ta=a+100

print("Total amount to be paid by the user is {:.2f} Rs.".format(ta))
