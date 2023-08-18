'''Consider a disk has 2 surfaces,each surface is divided into T tracks and each track is divided into S sectors, each sector is divided
into B blocks. Each block has 512 bytes of memory. So find the capacity of the disk(in KB's).
( Take T , S and B by the user)
Explanation: Capacity = 2xTxSxBx512 bytes.
1KB =1024 bytes
So Capacity in KB = Total Capacity in bytes/1024'''
t,s,b=map(int,input("Enter the number of tracks, sectors and blocks: ").split())
b=2*t*s*b*512
kb=b/1024
print("Capacity of the disk = {:.2f} kilobytes".format(kb))
