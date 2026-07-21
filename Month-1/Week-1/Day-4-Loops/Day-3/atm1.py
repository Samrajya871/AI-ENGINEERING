#the program will close after a choice since we haven't used loops

balance =10000
print(" 1. Check Balance \n 2. Deposit \n 3. Withdraw \n4. Exit")

choice= int(input("Enter a choice:"))

if choice==1:
    print(f"The balance is {balance}")
elif choice==2:
    deposit=int(input("Enter the amount to deposit"))
    balance+=deposit
    print(f"The new balance is {balance}")
elif choice==3:
    withdraw=int(input("Enter the amount to withdraw"))
    if withdraw<0:
        print("amount can't be negative")
    else:
        if withdraw>balance:
            print("Insufficient Balance")
        else:
            balance-=withdraw
            print(f"The new balanes is {balance}")
elif choice ==4:
    print("Thanks for using the ATM")

else:
    print("Not a choice")

