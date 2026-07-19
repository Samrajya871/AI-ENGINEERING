def get_marks():
    marks=int(input("Enter the marks"))
    return marks

def calculate_grade(marks):
    if marks<0 or marks>100:
        return ("invalid") 
    elif marks>=90:
        return ("A+")
    elif marks>=80:
        return "A"
    elif marks>=70:
        return "B"
    elif marks>=60:
        return "C"
    elif marks>=50:
        return "D"
    else:
        return "F"
    

def report(name,marks,grade):
    print("-----Student Report------")

    if grade=="invalid":
        print("Invalid marks entered")
    else:
        print("Name: ", name)
        print("Marks: ",marks)
        print("Grade: ",grade)


#Main program

while True:
    name=input("Enter the student's name: ")

    marks=get_marks()
    grade=calculate_grade(marks)

    report(name,grade,marks)

    choice=input("Do you want to enter another student's marks(Yes/No)")

    if choice.lower()!="yes":
        print("\n Thanks")
        break


