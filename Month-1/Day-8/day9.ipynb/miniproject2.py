with open("journal.txt","a")as file:
    date=input("Enter the date: ")
    mood=input("Enter the mood u are on: ")
    entry=input("Enter what u want to write on journal:")
    file.write(date + "\n")
    file.write(f"Mood: {mood} \n" )
    file.write(entry+ "\n")
