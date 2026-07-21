from validation import validate_age, validate_marks
students=[]


def add_students(students):
    name=input("Enter Student name: ")

    try:
        age=int(input("Enter age: "))
        validate_age(age)

        marks=float(input("Enter Marks: "))
        validate_marks(marks)
    
    except ValueError as e:
        print(e)
        return
    
    student={
        "name": name,
        "age": age,
        "marks": marks
    }

    students.append(student)
    print("Student Added Successfully")


def delete_student(students):
    name=input("Enter student name to delete: ")

    for student in students:
        if student["name"].lower()==name.lower():
            students.remove(student)
            print("Student Deleted successfully! ")
            return
     
    print("Student not found")
        
