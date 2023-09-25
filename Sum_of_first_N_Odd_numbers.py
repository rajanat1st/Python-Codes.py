# Write a program to find Sum of first n Odd numbers.
n=int(input("Enter the number of eliments: "))
s=0
for i in range(1,n+1,2):
    s+=i
print(f"Sum of first {n} Odd numbers = {s}")
