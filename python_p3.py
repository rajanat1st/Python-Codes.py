'''You are given that a mango weighs X kilograms and a truck weighs Y kilograms. You want to crossa bridge that can withstand a
wdeight of Z kilograms. Find the maximum number of mangoes you can load in the truck so that you can cross the bridge safely
( Take X , Y and Z from the console).
It is guaranteed that X<=Y<=Z'''
x=float(input("Enter the weight of a mango (in Kg): "))
y=int(input("Enter the weight of the truck (in Kg): "))
z=int(input("Enter the weight the bridge can withstand (in Kg): "))
m=(z-y)/x
print("Maximum number of mangoes you can load in the truck = ",int(m))



