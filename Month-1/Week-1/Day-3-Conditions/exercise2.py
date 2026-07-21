admin_username = "samrajya"

admin_password = "python123"

user = input("Enter the username:\n")

password = input("Enter the password:\n")

if user==admin_username and password==admin_password:
    print("Successfully logged in")
else:
    print("Invalid credentials")