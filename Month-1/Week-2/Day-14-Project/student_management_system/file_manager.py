import json
from models import Student
path=r"C:\Users\samra\Videos\AI-Enginnering-Bootcamp\Month-1\Week-2\Day-14-Project\student_management_system\student.json"
def save_students(students):
    data=[]

    for student in students:
        s1={
        "name": student.name,
        "student_id": student.student_id,
        "age": student.age,
        "course": student.course,
        "marks": student.marks
           }
        data.append(s1)

    with open(path,"w")as file:
        json.dump(data,file,indent=4)

def load_students():
    try:
        with open(path,"r")as file:
            data=json.load(file)
            students=[]

            for student_dict in data:
                student=Student(
                    student_dict["name"],
                    student_dict["student_id"],
                    student_dict["age"],
                    student_dict["course"],
                    student_dict["marks"]
                )
                students.append(student)
            return students
    except (FileNotFoundError, json.JSONDecodeError):
        return []

