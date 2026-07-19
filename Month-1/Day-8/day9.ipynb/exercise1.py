count=0
with open("notes.txt", "r") as file:
    for line in file:
        print(len(line))