# Write a program to compute the Compound Interest (CI) when Principal (P),Rate of interest (R) and Tme period (T) are given.
p=int(input("Enter the principal amount: "))
r=float(input("Enter the rate of interest: "))
t=float(input("Enter the time period in years: "))
amt=p*(1+r/100)**t
ci=amt-p
print("The compound interest is {:.2f} Rs".format(ci)) 
