name = input("What is your name?")

age=int(input("What is your age?"))

country=input("What is Your Country name?")

fav_subj=input("What is your favourite subject?")

marks=int(input(f"How much did u get on {fav_subj}:"))
if(marks<0 or marks>100):
    print("Error")
else:

    print("-----Student Report-----")
    print(f"Name:{name}")
    print(f"Age:{age}")
    print(f"Country:{country}")
    print(f"Subject:{fav_subj}")
    print(f"Marks:{marks}")

    if marks>=90 :
        print("Excellent")
    elif marks>=75:
        print("Good")
    else:
        print("Keep Practicing") 