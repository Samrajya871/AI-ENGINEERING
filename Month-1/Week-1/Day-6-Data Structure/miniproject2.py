cart=[]

def show_menu():
    print("1 Add Item\n2 Remove Item\n3 View Cart\n4 Exit")

def add_item(cart):
    item=input("Enter the item: ").lower() #converts item in lowercase 
    if item not in cart:
        cart.append(item)
        print(f"{item} has been added to cart\n")
    else:
        print("Item already in the cart")

def remove_item(cart):
    item=input("Enter the item to remove:")
    if item in cart:
        cart.remove(item)
        print(f"{item} has been removed from cart")
    else:
        print("Item not found")

def view_cart(cart):
    print("----------Cart History----------")
    if len(cart)==0:
        print("Empty Cart")
    else:
        for i,item in enumerate(cart, start=1):
            print(f"{i}. {item}")
    print("--------------------------")

while True:
    show_menu()
    choice=int(input("Enter a choice: "))

    if choice==1:
        add_item(cart)
    elif choice==2:
        remove_item(cart)
    elif choice==3:
        view_cart(cart)
    elif choice==4:
        print("Thanks")
        break
    else:
        print("NO CHOICE")





