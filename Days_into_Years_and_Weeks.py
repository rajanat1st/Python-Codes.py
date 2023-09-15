# Write a program to convert specified days into years and weeks
d=int(input("Enter the number of days: "))
y=d//365
w=(d%365)//7
print(d,"Days =",y,"Years and",w,"Weeks")
