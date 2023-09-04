'''Most programmers will tell you that one of the ways to improve your performance in competitive programming is to practice a lot
of problems.
Ben took the above advice very seriously and decided to set a target for himself.
Ben decides to solve at least 10 problems every week for 4 weeks and took an oath to do that.
Given the number of problems he actually solved in each week over 4 weeks as P1, P2, P3, P4.
Determine if he fulfilled his oath or not.'''
p1,p2,p3,p4=map(int,input("Ente the number of problems Ben solved over 4 weeks: ").split())
if p1<10 or p2<10 or p3<10 or p4<10:
    print("Ben did not fulfill his oath")
else:
    print("Ben fulfilled his oath")
    
