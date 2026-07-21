name = input("Enter a student's name:\n")

marks= int(input("Enter the marks obtained:\t"))

if marks<0 or marks>100:
    print("Wrong")
else:
    if marks>=90:
        print("A+")
    elif marks>=80:
        print("A")
    elif marks>=70:
        print("B")
    elif marks>=60:
        print("C")
    elif marks>=50:
        print("D")
    else:
        print("Fail")

if marks>80:
    print(f"Congratulations {name}")
else:
    print(f"Try haeder nect time {name}")
