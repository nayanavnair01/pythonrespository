'''
Author: Nayana V Nair
Date:  19/10/2024
Description: Simple desktop calculator using Python.
 Only the five basic arithmetic operators.
'''
number1=int(input("Enter your num1:"))
number2=int(input("Enter your num2:"))
number3=int(input("Enter your num3:"))
sum=(number1+number2)
print("sum of num1 and num2 is:",sum)
difference=(number1-number2)
print("The difference when num2 is subtracted from num1 is:",difference)
product=number1*number2
print("The product of num1 and num2 is:",product)
division=(number1/number2)
print("The quotient when num1 is divided by num2 is:",division)
print("the remainder when num1 is divided by num2 is:",number1%number2)
print("he result of (num1 + num2) * num3 / 2 is:",(number1+number2)*number3/2)