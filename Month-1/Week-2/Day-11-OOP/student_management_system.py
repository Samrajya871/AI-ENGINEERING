class Student:
    def __init__(self,SID,Name,Age):
        self.SID=SID
        self.name=Name
        self.age=Age
        self.marks=[]

    def add_marks(self,mark):
        if 0<=mark <=100:
            self.marks.append(mark)
            print("Marks added successfully")
        else:
            print("Invalid Mark. Enter marks between 0 and 100")
    
    def average_marks(self):
        if len(self.marks)==0:
            return 0
        return sum(self.marks)/len(self.marks)
    
    def display_students(self):
        print("\nStudent Details")
        print("-------------------------")
        print("Student Id :",self.SID)
        print("Name :",self.name)
        print("Age :",self.age)
        print("Marks :",self.marks)
        print("Average :",round(self.average_marks(), 2))
        print("--------------------------") 


students=[]
while True:
    print("------Student Report--------")
    print("1 Add Student\n2 Add Marks\n3 Display Student\n4 Display All Students\n5 Exit")
    print("----------------------------")
    try:
        choice=int(input("Enter the choice: "))
        if choice==1:
            sid=input("Enter Student Id: ")
            name=input("Enter the name: ")
            age=int(input("Enter the age of the student: "))

            s1=Student(sid,name,age)
            students.append(s1)

            print("Student Added Successfully")
        
        elif choice==2:
            sid=input("Enter the student Id: ")
            found=False
            for s in students:
                if s.SID == sid:
                    mark=float(input("Enter the marks: "))
                    s.add_marks(mark)
                    found=True
                    break
            
            if not found:
                print("Student not found")

        
        elif choice==3:
            sid=input("Enter the student id: ")
            found=False
            for s in students:
                if s.SID==sid:
                    s.display_students()
                    found=True
                    break
            
            if not found:
                print("Student not found")

        elif choice==4:
            if len(students)==0:
                print("No students available")

            else:
                for s in students:
                    s.display_students()
        
        elif choice==5:
            print("Closing.....")
            break

        else:
            print("Invalid")

    except ValueError as e:
        print(e)




    