import json
filename=r"C:\Users\samra\Videos\AI-Enginnering-Bootcamp\Month-1\Day-10\module\student utility\student.json"
def save_students(filename, students):
    with open(filename, "w")as file:
        json.dump(students, file, indent=4)

    print("Data saved successfully")

def load_students(filename):
    try:
        with open(filename,"r")as file:
            students=json.load(file)

        print("Data loaded successfully")
        return students
    except FileNotFoundError:
        return []