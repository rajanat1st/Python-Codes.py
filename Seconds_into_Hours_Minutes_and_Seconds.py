# Write a program to convert given seconds (integer) into hours, minutes and seconds
sec=int(input("Enter the seconds: "))
h=sec//3600
m=(sec%3600)//60
s=(sec%3600)%60
print("{} seconds = {}h:{}m:{}s".format(sec,h,m,s))
