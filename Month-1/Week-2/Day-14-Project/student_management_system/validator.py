
def validate_name(name):
    if not name or not name.strip():
        raise ValueError("Name cannot be empty or consist only of spaces.")


def validate_age(age):
    if age<=0:
        raise ValueError("Age must be greater than zero")

def validate_marks(marks):
    if marks<0 or marks>100:
        raise ValueError("Marks cannot less than zero or greater than 100")

def validate_duplicate_id(student_id, students):
    for student in students:
        if student.student_id==student_id:
            raise ValueError("Id already exists.")
