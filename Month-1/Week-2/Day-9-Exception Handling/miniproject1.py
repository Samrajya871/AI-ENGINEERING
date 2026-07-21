def show_menu():
    print("--------Calculator---------")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    print("---------------------------")


def add():
    try:
        total=int(input("Enter total no of numbers u want to add:"))
        if total<=0:
            print("Enter a positive number")
            return
        
        total_sum=0

        for i in range(total):
        
            num=float(input(f"Enter value of no. {i+1}: "))
            total_sum+=num
        print("Sum = ",total_sum)
    except ValueError:
        print("Enter a valid number")
    
def sub():
    try:
        total=int(input("Enter total no of numbers u want to sub:"))
        if total<=0:
            print("Enter a positive number")
            return
        
        result=float(input("Enter value of no. 1:"))

        for i in range(1, total):
        
            num=float(input(f"Enter value of no. {i+1}: "))

            result-=num
        print("Result= ",result)
    except ValueError:
        print("Enter a valid number")


def mul():
    try:
        total=int(input("Enter total no of numbers u want to mul:"))
        if total<=0:
            print("Enter a positive number")
            return
        
        product=float(input("Enter value of no. 1:"))

        for i in range(1, total):
        
            num=float(input(f"Enter value of no. {i+1}: "))

            product*=num
        print("Result= ",product)
    except ValueError:
        print("Enter a valid number")
       
def div():
    try:
        total=int(input("Enter total no of numbers u want to divide:"))
        if total<=0:
            print("Enter a positive number")
            return
        
        result=float(input("Enter value of no. 1:"))

        for i in range(1, total):
        
            num=float(input(f"Enter value of no. {i+1}: "))

            if num==0:
                print("Cannot be divide by zero")
                return

            result/=num
        print("Result= ",result)
    except ValueError:
        print("Enter a valid number")


while True:
    show_menu()
    try:
        choice=int(input("Enter the choice: "))

        if choice==1:
            add()
        elif choice==2:
            sub()
        elif choice==3:
            mul()
        elif choice==4:
            div()
        elif choice==5:
            print("Thanks")
        else:
            print("Invalid")
    except ValueError:
        print("Enter correct choice")

