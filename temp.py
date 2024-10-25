'''
Author:Nayana V Nair
Date:25/10/2024
Description:Write a Python program to convert temperature values back and
forth between Celsius and Fahrenheit. The user should be able to input a temperature in Celsius or
 Fahrenheit, and the program should convert it to the other unit
'''
temp1=int(input("Enter temperature"))
unit=input("Is this in (C)elsius or (F)ahrenheit?")
f = (9 / 5 * temp1) + 32
if  unit=="c":

    print(temp1 , "celsius is ", f,"fahrenheit")
else:
    c=5/9*(temp1-32)
    print(temp1,"fahrenheit is",c, "celsius")
