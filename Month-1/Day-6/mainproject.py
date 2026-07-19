contacts = {
    "Ram":"9800000000",
    "Hari":"9811111111"
}

def menu():
    print("1 Add Contact\n2 Search Contact\n3 Delete Contact\n4 View All\n5 Exit")



def add_contact(contacts):
    name=input("Enter the name: ").lower()
    contact=input("Enter the contact: ")
    contacts[name]=contact
    print("The contact has been added")


def search_contact(contacts):
    name=input("Enter the name: ")
    if name in contacts:
        contact=contacts[name]
        print("Contact: ",contact)
    else:
        print("Contact doesn't exist")

def delete_contact(contacts):
    name=input("Entet the name: ")
    if name in contacts:
        contacts.pop(name)
        print(f"{name} has been removed")
    else:
        print("No such contacts\n")

def search_all(contacts):
    print("----------Contact Management System-----------")

    for x,y in contacts.items():  #loops through both key and values
        print(f"Name: {x}")
        print(f"Contacts: {y}")
    print("-----------------------------")
while True:
    menu()
    choice=int(input("Enter the choice: "))

    if choice==1:
        add_contact(contacts)
    elif choice==2:
        search_contact(contacts)
    elif choice==3:
        delete_contact(contacts)
    elif choice==4:
        search_all(contacts)
    elif choice==5:
        print("Thanks")
        break
    else:
        print("Invalid")

