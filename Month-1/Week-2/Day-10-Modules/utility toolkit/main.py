from calculator import calculator
from converter  import converter

def menu():
    print("------Utility Tool------")
    print("1. Calculator")
    print("2. Converter")
    print("3. Exit")
    print("-" * 24)

while True:
    try:
        menu()
        choice=int(input("Enter the choice(1-3): "))

        if choice==1:
            calculator()
        elif choice==2:
            converter()
        elif choice==3:
            print("Thanks")
            break
        else:
            print("Invalid")

    except ValueError:
        print("Nahh")
