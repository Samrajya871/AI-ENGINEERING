transactions=[]
balance=0.0
next_id=1

def show_menu():
    print("====== PERSONAL FINANCE MANAGER ======")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Balance")
    print("4. View Transactions")
    print("5. Delete Transaction")
    print("6. Monthly Summary")
    print("7. Exit")
    print("--------------------------------------")

def add_income(transactions,balance,next_id):
    category=input("Enter the category")
    amount=int(input("Enter the amount: "))
    description=input("Enter the description for the amount: ")
    if amount<=0:
        print("Income can't be less than zero")
    else:
        new_tx={
            "id":next_id,
            "type":"income",
            "amount":amount,
            "category":category,
            "description":description

        }
        transactions.append(new_tx)
        balance+=amount
        next_id+=1
        print("Income added successfully")
        with open("manager.txt", "a") as file:
            file.write(str(new_tx)+ "\n")
    return balance,next_id 
    



def add_expense(transactions,balance,next_id):
    category=input("Enter the category")
    amount=int(input("Enter the amount: "))
    description=input("Enter the description for the amount: ")
    if amount<=0:
        print("Expense can't be less than zero")
    else:
        new_tx={
            "id":next_id,
            "type":"expense",
            "amount":amount,
            "category":category,
            "description":description
        }

        transactions.append(new_tx)
        balance-=amount
        next_id+=1
        print("Expenses added successfully")
        with open("manager.txt", "a") as file:
                        file.write(str(new_tx) + "\n")

    return balance,next_id

def view_balance(balance):
    print("\n----------Current Balance---------")
    print("Your Balnace is Rs.", balance)

def view_transactions(transactions):
    print("------Transaction History------")
    if len(transactions)==0:
        print("No transactions found yet")
    else:
        for tx in transactions:
            print("Id:", tx["id"], "\nType:", tx["type"],"\nCategory:", tx["category"], "\nAmount:", tx["amount"], "\nDescription:", tx["description"])

def delete_transactions(transactions,balance):
    choice=int(input("Enter the transaction you want to delete: "))
    for index, i in enumerate(transactions):
        if i["id"]==choice:
            if i["type"]=="income":
                balance-=i["amount"]
            else:
                balance+=i["amount"]
            transactions.pop(index)
            print("Transaction Deleted Successfully")
            return balance
        
    print("No such transactions")
    return balance

def monthly_summary(transactions):
    print("------Summary----------")
    total_income=0.0
    total_expenses=0.0

    for tx in transactions:
        if tx["type"]=="income":
            total_income=total_income+tx["amount"]
        else:
            total_expenses=total_expenses+tx["amount"]
        
    
    print("Total Income Added: Rs.", total_income)
    print("Total Expenses recorded: Rs.", total_expenses)
    print("Current Balnce", (total_income-total_expenses))
    print("Total No of transactions", len(transactions))

while True:
        show_menu()
        choice=int(input("Select an option(1-7):"))

        if choice==1:
            balance=add_income(transactions,balance,next_id)
        elif choice==2:
            balance=add_expense(transactions,balance,next_id)
        elif choice==3:
            view_balance(balance)
        elif choice==4:
            view_transactions(transactions)
        elif choice==5:
            balance=delete_transactions(transactions,balance)
        elif choice==6:
            monthly_summary(transactions)
        elif choice==7:
            print("Thanks for using")
            break
        else:
            print("Invalid option")
