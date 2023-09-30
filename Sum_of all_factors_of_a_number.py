# Write a program to print the Sum of all factors of a number.
n=int(input("Enter a number: "))
s=0
for i in range(1,n+1):
    if n%i==0:
        s+=i
print(f"Sum of all factors of {n} = {s}")
