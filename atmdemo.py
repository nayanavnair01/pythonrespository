balance_amount=1000
while True:
    print("\n1.\tCheck Balance")
    print("2.\tDeposite Money")
    print("3.\tWithdraw Money")
    print("4.\tExit")
    choice=int(input("Enter Your Choice:"))
    if choice==1:
        print(f"The current balance ${balance_amount}")
    elif choice==2:
        deposite_amount=float(input("Enter the amount:"))
        balance_amount =deposite_amount + balance_amount
        print(f"the deposited amount ${deposite_amount} and "f"the current balance ${balance_amount}")
    elif choice==3:
        withdraw_amount =float(input("Enter the amount to withdraw amount:"))
        if withdraw_amount>balance_amount:
            print("insufficient balance")
        else:
            balance_amount = balance_amount - withdraw_amount
            print(f"The amount withdraw from the account "f"${withdraw_amount} the balance amount"f"{balance_amount}")
    elif choice==4:
        break
    else:
        print("invalid entry")
