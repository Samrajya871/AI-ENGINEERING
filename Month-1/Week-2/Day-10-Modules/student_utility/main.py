from student import add_students, delete_student, students
from grades import calculate_average, calculate_grade
from file_handler import save_students, load_students
file_path=r"C:\Users\samra\Videos\AI-Enginnering-Bootcamp\Month-1\Week-2\Day-10-Modules\student_utility\student.json"

students.extend(load_students(file_path))


def display_students():
    if not students:
        print("No students found.")
        return

    print("\n------ Student Records ------")

    for student in students:
        grade = calculate_grade(student["marks"])

        print(f"Name  : {student['name']}")
        print(f"Age   : {student['age']}")
        print(f"Marks : {student['marks']}")
        print(f"Grade : {grade}")
        print("-----------------------------")

    avg = calculate_average(students)
    print(f"Class Average: {avg:.2f}")


while True:
    print("\n===== Student Utility Package =====")
    print("1. Add Student")
    print("2. Delete Student")
    print("3. View Students")
    print("4. Save")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_students(students)

    elif choice == "2":
        delete_student(students)

    elif choice == "3":
        display_students()

    elif choice == "4":
        save_students(file_path, students)

    elif choice == "5":
        save_students(file_path, students)
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")