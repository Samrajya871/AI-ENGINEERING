password="python123"

for i in range(3):
    word=input("Enter the password:")
    if word==password:
        print("Logged in")
        break
    elif i<2:
        print("Try again")
    else:  
        print("Account locked")