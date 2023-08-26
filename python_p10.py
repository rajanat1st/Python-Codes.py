# Write a program to extract the last two digits of a given year
import sys
y=int(input("Enter the year: "))
if y>0 and y<10:
    print("Entered year only contains single digit",y)
    sys.exit()
else:
    y=y%100
    print("The last two digits of the entered year are",y) 
