'''
Author: Nayana V Nair
Date:22/11/2024
Description:Program to construct patterns of stars (*), using a nested for loop.
'''
row=int(input("Enter no of row:"))
for i in range(row):
    for j in range(i+1):
        print("*",end="")
    print("")

row=int(input("Enter no of row:"))
for i in range(row):
    for j in range(row-i):
        print("*",end="")
    print("")

n=int(input("Enter no of row:"))
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for k in range (2*i-1):
        print("*",end="")
    print("  ")

n=int(input("Enter no of row:"))
for i in range(n,0,-1):
    for j in range(n-i):
        print(" ", end="")
    for k in range(2*i-1):
        print("*",end=" ")
    print()

