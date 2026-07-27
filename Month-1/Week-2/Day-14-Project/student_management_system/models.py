class Student:
    def __init__(self,name,student_id,age,course,marks):
        self.name=name
        self.student_id=student_id
        self.age=age
        self.course=course
        self.marks=marks

    def calculate_grade(self):
        if self.marks>=90:
            return "A+"
        elif self.marks>=80:
            return "A"
        elif self.marks>=70:
            return "B"
        elif self.marks>=60:
            return "C"
        elif self.marks>=50:
            return "D"
        elif self.marks>=40:
            return "E"
        else:
            return "F"

    def display(self):
        print("Name:",self.name)
        print("ID:",self.student_id)    
        print("Age:",self.age)
        print("Course:",self.course)
        print("Marks:",self.marks)
        print("Grade:",self.calculate_grade())

