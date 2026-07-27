from validator import validate_name, validate_age, validate_marks, validate_duplicate_id
from models import Student
from file_manager import load_students, save_students
students=load_students()
while True:
    print("====== STUDENT MANAGEMENT ======\n1. Add Student\n2. View Students\n3. Search Student\n4. Update Student\n5. Delete Student\n6. Sort Students\n7. Statistics\n8. Exit")
    choice=int(input("Enter the choice(1-8): "))

    if choice==1:
        try:
            name=input("Enter the student's name: ")
            stu_id=input("Enter the student's id: ")
            age=int(input("Enter the student's age: "))
            course=input("Enter the course: ")
            marks=int(input("Enter the marks: "))

            validate_name(name)
            validate_age(age)
            validate_marks(marks)
            validate_duplicate_id(stu_id, students)

            s1 = Student(name,stu_id,age,course,marks)

            students.append(s1)
            print("Student has been added")

        except ValueError as e:
            print(e)
    elif choice==2:
        if not students:
            print("No students found")
        else:
            for student in students:
                student.display()
                print("-" * 30)

    elif choice==3:
        search_id=input("Enter student Id: ")
        found=False
        for student in students:
            if student.student_id==search_id:
                student.display()
                found=True
                break
        if not found:
            print("Student not found")

    elif choice==4:
        stu_id=input("Enter student Id: ")
        for student in students:
            if student.student_id==stu_id:
                try:
                    new_name = input("Enter new name: ")
                    new_age = int(input("Enter new age: "))
                    new_course = input("Enter new course: ")
                    new_marks = int(input("Enter new marks: "))

                    validate_name(new_name)
                    validate_age(new_age)
                    validate_marks(new_marks)

                    student.name=new_name
                    student.age=new_age
                    student.course=new_course
                    student.marks=new_marks
                    print("Student updated successfully")
                    break
                except ValueError as e:
                    print(e)
        else:
            print("Student not found")

    elif choice==5:
        delete_id=input("Enter student ID to delete: ")
        for student in students:
            if student.student_id==delete_id:
                students.remove(student)
                print("Student deleted successfully")
                break

        else:
            print("Student not found.")

    elif choice==6:
        print("Sorting MENU")
        print("1. Sort by Name")
        print("2. Sort by Marks")
        print('3. Sort by Age')

        sort_choice=int(input("Enter your choice: "))

        if sort_choice==1:
            if not students:
                print("No students available")
            else:
                students.sort(key=lambda student:student.name)
                for student in students:
                    student.display()
                    print("-" * 30)

        elif sort_choice==2:
            if not students:
                print("No students available")
            else:
                students.sort(key=lambda student:student.marks)
                for student in students:
                    student.display()
                    print("-" *30)

        elif sort_choice==3:
            if not students:
                print("No students Available")
            else:
                students.sort(key=lambda student:student.age)
                for student in students:
                    student.display()
                    print("-" * 30)
        else:
            print("Invalid")

    elif choice==7:
        if not students:
            print("No students available")
        else:
            print("Total Students:",len(students))
            print("Highest Marks:",max(student.marks for student in students))
            print("Lowest Marks:",min(student.marks for student in students))
            print("Average Marks:",sum(student.marks for student in students)/len(students))
            count1=0
            for student in students:
                if student.calculate_grade() in ("A", "A+"):
                    count1 += 1
            print("No of A grades:",count1)

            count2=0
            for student in students:
                if student.calculate_grade() == "F":
                    count2 +=1
            print("No of Failed students:",count2)

    
    elif choice==8:
        save_students(students)
        print("Students saved successfully")
        print("Exiting...")
        break
    else:
        print("Invalid")
