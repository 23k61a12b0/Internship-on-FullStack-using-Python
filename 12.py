age=18
if age >18:
    print("eligible to vote")
else:
    print("not eligible to vote")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username == "admin" and password =="1234":
        print("login successful")
    else:
        print("invalid credentials")