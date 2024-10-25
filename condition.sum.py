'''
Author: Nayana V Nair
Date:25/10/2024
Description: sum of numbers
'''
number=int(input("Enter a number"))
sum_of_digits=0
while number>0:
    reminder =number%10
    sum_of_digits=sum_of_digits+reminder
    number = number//10
print("sum of digits of the given number:",sum_of_digits)