contacts = {
    "ram": {
        "phone": "9800000000",
        "email": "ram@gmail.com"
    },
    "hari": {
        "phone": "9811111111",
        "email": "hari@gmail.com"
    }
}
def menu():
    print("----------------Menu------------")
    print("1.View Full Contact\n2.Search by Name\n3.Update Phone\n4.Update Email\n5.Delete Contact")
    print("--------------------------------")

def view(contacts):
    for x, obj in contacts.items():
        print(x)
        for y in obj:
            print(y + ':', obj[y])

def search(contacts):
    name=input("Enter the name").lower()
    if name in contacts:
        print(contacts[name])
    else:
        print("No such contacts")


def update_phone(contacts):
    name=input("Enter the name of the person whose phone u want to change: ").lower()
    if name in contacts:
        new_phone=input("Enter the phone number")
        contacts[name]["phone"]=new_phone
    else:
        print("No such contact")



def update_email(contacts):
    name=input("Enter the name of the person whose email u want to change: ").lower()
    if name in contacts:
        new_email=input("Enter the email")
        contacts[name]["email"]=new_email
    else:
        print("No such contact")

def delete(contacts):
    name=input("Enter the contact u want to delete").lower()
    if name in contacts:
        contacts.pop(name)
    else:
        print("No such contacts")


while True:
    menu()
    choice=int(input("Enter the choice: "))

    if choice==1:
        view(contacts)
    elif choice==2:
        search(contacts)
    elif choice==3:
        update_phone(contacts)
    elif choice==4:
        update_email(contacts)
    elif choice==5:
        delete(contacts)
    elif choice==6:
        print("Thanks")
        break
    else:
        print("Invalid")
