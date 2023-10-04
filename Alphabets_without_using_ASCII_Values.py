# Program to print Alphabets without using ASCII Values.
print("Alphabets from A to Z: ")
for i in range(ord('A'),ord('Z')+1):
    print(chr(i),end=" ")
print("\n")
print("Alphabets from a to z: ")
for i in range(ord('a'),ord('z')+1):
    print(chr(i),end=" ")
