# Write a program to find whether a character is Uppercase or Lowercase.

ch=input("Enter an alphabet: ")
if ch.isupper():
    print(ch,"is an uppercase")
elif ch.islower():
    print(ch,"is a lowercase")
else:
    print(ch,"is not an alphabet!")
