''' Write a program that takes marks of five subjects, Physics, Chemistry, Biology, Mathematics and Computer Science as input and calculate 
percentage and grade according to given conditions:

If percentage >= 90%: Print: Grade A
If percentage >= 80%: Print: Grade B
If percentage >= 70%: Print: Grade C
If percentage >= 60%: Print: Grade D
If percentage >= 40%: Print: Grade E
If percentage < 40%: Print: Grade F '''

p=int(input("Enter the marks in Physics: "))
c=int(input("Enter the marks in Chemistry: "))
m=int(input("Enter the marks in Mathematics: "))
b=int(input("Enter the marks in Biology: "))
cs=int(input("Enter the marks in Computer Science: "))
pcg=(p+c+m+b+cs)/5
if pcg>=90:
    g='A'
elif pcg>=80:
    g='B'
elif pcg>=70:
    g='C'
elif pcg>=60:
    g='D'
elif pcg>=40:
    g='E'
else:
    g='F'
print("Percentage =","%.2f"%pcg,"%","\nGrade =",g)
#print("Percentage ={:.2f} %\nGrade = {}".format(pcg,g))
