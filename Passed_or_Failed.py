''' Given the marks (out of 100) of 5 different subjects viz. English, Maths, Physics, Chemistry and Computer Science. Determine if the student is PASSED
or FAILED in exam.
A student is considered as PASS, if and only if he/she gets more than 34 marks in EACH and EVERY subject. '''
import sys
def result(n):
    e=int(input("Enter the marks in English: "))
    m=int(input("Enter the marks in Maths: "))
    p=int(input("Enter the marks in Physics: "))
    c=int(input("Enter the marks in Chemistry: "))
    cs=int(input("Enter the marks in Computer Science: "))
    if e<=100 and m<=100 and p<=100 and c<=100 and cs<=100:
        if e>34 and m>34 and p>34 and c>34 and cs>34:
            print("\nThe student is PASSED")
        else:
            print("\nThe student is FAILED")
            sys.exit(0)
    else:
        print("\nIndividual subject's marks should not be greater than 100! Please enter valid marks again.")
        result(1)
    
e=int(input("Enter the marks in English: "))
m=int(input("Enter the marks in Maths: "))
p=int(input("Enter the marks in Physics: "))
c=int(input("Enter the marks in Chemistry: "))
cs=int(input("Enter the marks in Computer Science: "))
if e<=100 and m<=100 and p<=100 and c<=100 and cs<=100:
        if e>34 and m>34 and p>34 and c>34 and cs>34:
            print("\nThe student is PASSED")
        else:
            print("\nThe student is FAILED")
            sys.exit(0)
else:
    print("\nIndividual subject's marks should not be greater than 100! Please enter valid marks again.")
    result(1)
