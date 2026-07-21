
def validate_age(age):
    if age<5 or age>100:
        raise ValueError("Invalid age")
    

def validate_marks(marks):
    if marks<0 or marks>100:
        raise ValueError("Marks must be between 0 and 100")