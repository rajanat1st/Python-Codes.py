''' Read an integer n from STDIN. Without using any string methods, try to print the following: 123...n
Print the list of integers from  through  as a string, without spaces. '''
n = int(input("Enter an integer: "))
for i in range(1,n+1):
    print(i,end="")
    i+=1
