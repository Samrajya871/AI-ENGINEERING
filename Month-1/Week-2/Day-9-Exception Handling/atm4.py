balance =10000
username="sam"
pin="1234"
history=[]
def verify_pin(username,pin):
    
    for attempt in range(3):
        try:
            attemptuser=input("Enter username: ")
            attemptpin=input("Enter pin: " )

            if not attemptuser.strip():
                raise ValueError("Username cannot be empty!")
            
            if not attemptpin.strip():
                raise ValueError("Pin cannot be empty")

            if attemptpin==pin and attemptuser==username:
                print("Login Successful")
                return True
            else:
                print(f"Invalid username or PIN. Attempts left: {2-attempt}")

        except ValueError as e:
            print(e)
            print(f"Attempts left: {2-attempt}")
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
    try:
        amount = float(input("Enter amount to deposit: "))

        if amount <=0:
            raise ValueError("Deposit amount must be greather than zero")
           
        else:
            balance += amount
            print("Deposit Successful")
            history.append(f"Deposited Rs. {amount}")

        return balance
    except ValueError as e:
        print(e)

def withdraw(balance,history):
    try:
        amount = float(input("Enter amount to withdraw: "))

        if amount <= 0:
            raise ValueError("Withdraw amount must be greater than zero")

        elif amount > balance:
            raise ValueError("Withdraw amount can't be more than balance.")

        else:
            balance -= amount
            print("Withdrawal Successful")
            history.append(f"Withdrew Rs.{amount}")

        return balance
    except ValueError as e:
        print(e)


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

if verify_pin(username,pin):
    while True:
        show_menu()
        try:
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
        except ValueError:
            print("Enter correct integer")