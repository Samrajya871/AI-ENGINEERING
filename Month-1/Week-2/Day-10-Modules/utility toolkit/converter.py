def show_menu():
    print("--------Calculator---------")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Kilometer to Miles")
    print("4. Exit")
    print("---------------------------")

def cel_fah():
    try:
        cel=float(input("Enter the Celsisu Degree: "))
        fah=((cel)*(9/5))+32
        print(f"{cel} Celsius is {fah} in Fahrenheit ")
    except ValueError:
        print("Wrong Input")

def fah_cel():
    try:
        fah=float(input("Enter the Celsisu Degree: "))
        cel=(fah-32)*(5/9)
        print(f"{fah} Fahrenheit is {cel} in Celsius ")
    except ValueError:
        print("Wrong Input")

def km_miles():
    try:
        km=float(input("Enter the Kilometer: "))
        miles=km*0.621371
        print(f"{km} Km is {miles} in Miles.")
    except ValueError:
        print("Wrong Input")

def converter():
    show_menu()
    choice()


def choice():
    while True:
        try:
            choice=int(input("Enter the choice: "))
            if choice==1:
                cel_fah()
            elif choice==2:
                fah_cel()
            elif choice==3:
                km_miles()
            elif choice==4:
                print("Thanks")
                break
            else:
                print("Invalid")
        except ValueError:
            print("Enter correct choice")