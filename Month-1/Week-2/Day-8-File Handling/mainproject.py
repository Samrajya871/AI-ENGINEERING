#student records manager
file_path=r"C:\Users\samra\Videos\AI-Enginnering-Bootcamp\Month-1\Week-2\Day-8-File Handling\students.txt"
def view_menu():
    print("-----------Students Record Manager------------")
    print("1. Add Students ")
    print("2. View Students")
    print("3. Search Students")
    print("4. Delete Student")
    print("5. Update Student")
    print("6. Exit")
    print("-----------------------------------------------")


def add_students(file_path):
    name=input("Enter the student's name: ")
    age=int(input("Enter the student's age: "))
    subject=input("Enter the subject student is studying: ")
    with open(file_path,"a")as file:
        file.write(f"\n{name},")
        file.write(f"{age},")
        file.write(f"subject\n")

def view_students(file_path):
    with open(file_path, "r")as file:
        for line in file:
            print(line.strip())

def search_students(file_path):
    name=input("Enter the student's name: ")
    found = False
    with open(file_path, "r")as file:
        for line in file:
            if line.startswith(name + ","): #startswith() checks if string starts with a certain value
                print(line.strip())
                found=True
                break
    if not found:        
        print("Name isn't in the system")
def del_student(file_path):
    name=input("Enter the name of the student whose details you want to delete: ")
    found= False
    with open(file_path, "r")as file:
        lines=file.readlines()
    
    with open(file_path, "w")as file:
        for line in lines:
            if line.startswith(name + ","):
                found = True
                continue
            file.write(line)

    if found:
        print("Deleted Successfully")
    else:
        print("No such Data")

def update_students(file_path):
    name=input("Enter the student's whose name u want to update: ")
    found=False
    with open(file_path, "r")as file:
        lines=file.readlines()
    
    with open(file_path, "w")as file:
        for line in lines:
            student=line.strip().split(",")

            if student[0]==name:
                age=input("Enter new age: ")
                subject=input("Enter new subject: ")

                file.write(f"{name},{age},{subject}\n ")
                found=True
            else:
                file.write(line)

    if found:
        print("File updated Successfully")
    else:
        print("No such data")

while True:
    view_menu()
    choice=int(input("Enter the choice (1-4): "))

    if choice==1:
        add_students(file_path)
    elif choice==2:
        view_students(file_path)
    elif choice==3:
        search_students(file_path)
    elif choice==4:
        del_student(file_path)
    elif choice==5:
        update_students(file_path)
    elif choice==6:
        print("Thanks for using")
        break
    else:
        print("Invalid choice")


