''' In a  coding contest, there are two types of problems:
Esay problems, which are worth 1 point each and Hard problems, which are worth 2 points each.
To qualify for the next round, a contestant must score at least X points. Professor solved A Easy problems and B Hard problems. Will Professor
qualify or not? (X,A and B are taken from the console) '''

x=int(input("Enter the minimum score to qualify: "))
a=int(input("Enter the Easy problems Professor solved: "))
b=int(input("Enter the Hard problems Professor solved: "))
ep=a
hp=b*2
if (ep+hp)>=x:
    print("Professor will qualify")
else:
    print("Professor will not qualify")
