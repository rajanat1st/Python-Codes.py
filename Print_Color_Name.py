''' Write a program to print the color name by taking the Color code as input.
V -> Violet, I -> Indigo, B -> Blue, G -> Green, Y -> Yellow, O -> Orange, R -> Red (Letters indicating colors are not case sensitive).
If none of the above characters mentioned is entered as input, print -1 as output. '''

ch=input("Enter the character: ")
if ch=='V' or ch=='v':
    print("Violet")
elif ch=='I'or ch=='i':
    print("Indigo")
elif ch=='B' or ch=='b':
    print("Blue")
elif ch=='G' or ch=='g':
    print("Green")
elif ch=='Y'or ch=='y':
    print("Yellow")
elif ch=='O' or ch=='o':
    print("Orange")
elif ch=='R' or ch=='r':
    print("Red")
else:
    print("-1")
