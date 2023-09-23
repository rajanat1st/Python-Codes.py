# Write a program to check whether a number is Palindrome or Not.
n=int(input("Enter a number: "))
n1=n
rev=0
while(n>0):
    r=n%10
    rev=rev*10+r
    n=n//10
if n1==rev:
    print(f"\n{n1} is a Palindrome")
else:
    print(f"\n{n1} is not a Palindrome")
