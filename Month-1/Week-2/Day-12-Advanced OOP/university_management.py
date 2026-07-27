#creating a parent class
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display(self):
        print("Name: ",self.name)
        print("Age: ",self.age)

#child class
class Student(Person):
    def __init__(self,sid,name,age): 
        super().__init__(name,age) #using parent's constructor
        self.sid=sid
        self.marks=[]

    def add_marks(self,mark):
        if 0<= mark <=100:
            self.marks.append(mark)
            print("Marks added successfully")
        else:
            print("Invalid Marks.")

    def average(self):
        if len(self.marks)==0:
            return 0
        return sum(self.marks)/len(self.marks)
    
    def display(self):
        super().display()
        print("Student Id:",self.sid)
        print("Marks: ",self.marks)
        print("Average:",self.average())


class Professor(Person):
    def __init__(self,name,age,department,salary):
        super().__init__(name,age)
        self.department=department
        self.salary=salary

    def display_professor(self):
        print("Name:",self.name)
        print("Age:", self.age)
        print("Department:", self.department)
        print("Salary: ", self.salary)


students_list=[] #to store student's data
professors_list=[] #to store professor's data
while True:
    print("-------MENU--------")
    print("1. ADD STUDENT")
    print("2. ADD PROFESSOR")
    print("3. DISPLAY STUDENTS")
    print("4. DISPLAY PROFESSORS")
    print("5. EXIT")
    print("--------------------")

    choice=int(input("Enter a choice(1-5): "))

    if choice==1:
        sid=input("Enter the student's Id: ")
        name=input("Enter the student's name: ")
        age=int(input("Enter the student's age: "))
        mark=int(input("Enter the marks: "))

        s1=Student(sid,name,age)
        s1.add_marks(mark)

        students_list.append(s1)
        print("Student added successfully")

    elif choice==2:
        name=input("Enter the professor's name: ")
        age=int(input("Enter the professor's age: "))
        department=input("Enter the department: ")
        salary=input("Enter the salary: ")

        p1=Professor(name,age,department,salary)

        professors_list.append(p1)
        print("Professor added successfully.")

    elif choice==3:
        if not students_list:
            print("No students found.")
        else:
            for s in students_list:
                s.display()
                print("---------------")

    elif choice==4:
        if not professors_list:
            print("No professors found.")
        else:
            for p in professors_list:
                p.display_professor()
                print("---------------")

    elif choice==5:
        print("Closing the menu.....")
        break

    else:
        print("Invalid")
