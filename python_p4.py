#Program to find average of n numbers
n=int(input("Enter the number of elements you want to enter: "))
print("Enter",n,"numbers: ")
lst=[]
for i in range(n):
    elem=int(input())
    lst.append(elem)
avg=sum(lst)/n
print("Average = {:.2f}".format(avg))
