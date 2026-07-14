age = int(input("Enter the age:\t"))
if age<0:
    print("Invalid age")
else:
    if age<12:
        print("The fee is 200")
    elif age<=17 and age>=12:
        student_id = input("Do u have an ID(Yes/No):\t")
        if student_id.lower()=="yes": #.lower() so user can type yes in lowercase or uppercase
            print(" The fee is 300")
        else:
            print("U should have an Student Id for the discount. The fee is 500")
    elif age<=59:
        print("The fee is 500")

    else:
        print("The fee is 250")
  
