import json

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