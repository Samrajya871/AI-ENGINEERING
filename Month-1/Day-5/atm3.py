balance =10000
pin="1234"
history=[]
def verify_pin(pin):
    
    for attempt in range(3):
        attemptpin=input("Enter pin: " )

        if attemptpin==pin:
            print("Pin verified")
            return True
        else:
            print("Try again")
    print("Account Locked")
    return False

def show_menu():
    print("\n===== ATM =====")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    print("5. View Transaction History")

def deposit(balance,history):
    amount = float(input("Enter amount to deposit: "))

    if amount > 0:
        balance += amount
        print("Deposit Successful")
        history.append(f"Deposited Rs. {amount}")
    else:
        print("Invalid amount")

    return balance

def withdraw(balance,history):
    amount = float(input("Enter amount to withdraw: "))

    if amount <= 0:
        print("Invalid amount")

    elif amount > balance:
        print("Insufficient Balance")

    else:
        balance -= amount
        print("Withdrawal Successful")
        history.append(f"Withdrew Rs.{amount}")

    return balance

def check_balance(balance):
    print("Current Balance:", balance)


def transaction(history):
    if len(history)==0:
        print("No history")
    else:
        print("\n --------Transaction History---------")
        for i,item in enumerate(history, start=1):
            print(f"{i}.{item}")
        print("-------------------------------------------")


#main program

if verify_pin(pin):
    while True:
        show_menu()
        choice=int(input("Enter a choice:"))

        if choice==1:
            check_balance(balance)
        elif choice==2:
            balance=deposit(balance,history)
        elif choice==3:
            balance=withdraw(balance,history)
        elif choice==4:
            print("Thanks for using the atm")
            break
        elif choice==5:
            transaction(history)

        else:
            print("Invalid")