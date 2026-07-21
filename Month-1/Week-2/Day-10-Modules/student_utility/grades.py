def calculate_average(students):
    if not students:
        return 0
    
    total=0

    for student in students:
        total+= student["marks"]


    return total/len(students)


def calculate_grade(marks):
    if marks>=90:
        return "A"
    elif marks>=80:
        return "B"
    elif marks>=70:
        return "C"
    elif marks>=60:
        return "D"
    else:
        return "F"