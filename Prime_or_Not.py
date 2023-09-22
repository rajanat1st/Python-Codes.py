# Write a program to find out whether a number is Prime or not.
n=int(input("Enter a number: "))
f=0
for i in range(2,n):
    if n%i==0:
        f+=1
if f>0:
    print(f"\n{n} is not a Prime number")
else:
    print(f"\n{n} is a Prime number")
