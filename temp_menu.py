 '''
 Author:Nayana V Nair
 Date:28/10/2024
 Description:Write a menu-driven Python program that allows users to convert temperatures between Celsius and Fahrenheit.
 '''
 while True:
    print("\n1.\tConvert Celsius to Fahrenheit")
    print("2.\tConvert Fahrenheit to Celsius")
    print("3.\tExit Program")
    choice=int(input("Enter your option:"))
    if choice==1:
        temp=int(input("Enter a temperature in celsius:"))
        f=(temp* 9/5) + 32
        print(f"the equivalent temperature in Fahrenheit {f}")
    elif choice==2:
        temp1=int(input("Enter a temperature in fahrenheit:"))
        c=(temp1 - 32) * 5/9
        print(f"the equivalent temperature in celsius {c}")
    elif choice==3:
        break
    else:
        print("invalid entry")






