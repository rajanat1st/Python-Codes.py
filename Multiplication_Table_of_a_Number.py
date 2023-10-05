# Write a program to print Multiplication table of given number.
n=int(input("Which number's multiplication tabel do you need? : "))
print()
for i in range(1,11):
    print("{}X{}={}".format(n,i,n*i))
