# Write a program to find Sum of first n Even numbers.
n=int(input("Enter the number of eliments: "))
s=0
for i in range(2,n+1,2):
    s+=i
print(f"Sum of first {n} Even numbers = {s}")
