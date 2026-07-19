def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if b==0:
        print("Cannot be zero")
    else:
        return a/b

while True:
    print("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Exit")

    choice=int(input("Enter a choice"))

    if choice >=1 and choice<=4:
        a=int(input("Enter the first number"))
        b=int(input("Enter the second number"))

    if choice==1:
       print("Answer =", add(a,b))
       
    elif choice == 2:
     print("Answer =", sub(a, b))

    elif choice == 3:
     print("Answer =", mul(a, b))

    elif choice == 4:
     print("Answer =", div(a, b))

    elif choice==5:
       print("Thanks")
       break


