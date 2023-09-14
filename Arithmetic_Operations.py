# Write a program to print all arithmetic operations on two given numbers
def arithmetic_operations(m,n):
    print("{}+{}={}".format(m,n,m+n))
    print("{}-{}={}".format(m,n,m-n))
    print("{}x{}={}".format(m,n,m*n))
    print("{}/{}={:.2f}".format(m,n,m/n))
m,n=map(int,input("Enter any two numbers: ").split())
arithmetic_operations(m,n)
