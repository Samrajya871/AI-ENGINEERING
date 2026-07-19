def menu():
    print("-------Simple Note Saver--------")
    print("1. Add notes\n")
    print("2. View Notes\n")
    print("3. Exit\n")
    print("--------------------------------")

def add_notes():
    notes=input("Enter the note: ")
    with open(r"C:\Users\samra\Videos\AI-Enginnering-Bootcamp\Month-1\Day-8\notesaver.txt","a")as file:
        file.write(notes)
        file.write("\t")
        

def view_notes():
    with open(r"C:\Users\samra\Videos\AI-Enginnering-Bootcamp\Month-1\Day-8\notesaver.txt","r")as file:
        content=file.read()
    print(content)

while True:
    menu()
    choice=int(input("Enter a choice"))

    if choice==1:
        add_notes()
    elif choice==2:
        view_notes()
    elif choice==3:
        print("Thanks for using")
        break
    else:
        print("Invalid")