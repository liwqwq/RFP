# Sample user list for demonstration purposes
userlist = [
    {"username": "user1", "password": "pass1", "name": "Alice"},
    {"username": "user2", "password": "pass2", "name": "Bob"}
]

# Function to register a new user
def register():
    new_user = {}
    new_user["username"] = input("Enter a new username: ")
    new_user["password"] = input("Enter a new password: ")
    new_user["name"] = input("Enter your name: ")

    # Check if the username already exists
    for user in userlist:
        if user["username"] == new_user["username"]:
            print("Username already exists. Please try again.")
            return False

    # Add the new user to the user list
    userlist.append(new_user)
    print("Registration successful! You can now log in.")
    
    return True

# Add a login authentication method
def verify_login(username, password):
    for user in userlist:
        if user["username"] == username and user["password"] == password:
            return user["name"]
    return None

# 
def login():
    attempts = 0
    while attempts < 3:
        uname = input("Username: ")
        upwd = input("Password: ")
        
        user_name = verify_login(uname, upwd)
        if user_name:
            print(f"Login successful! Welcome, {user_name}.")
            return True
        else:
            attempts += 1
            print(f"Invalid credentials! {3 - attempts} attempt(s) remaining.")
    print("Too many failed attempts. User is locked.")
    return False


# Login function
def login():
    msg = "failed"
    count = 0
    while True:
        uname = input("Please enter your username: ")
        upwd = input("Please enter your password: ")
        for user in userlist:
            if uname == user["username"] and upwd == user["password"]:
                print("Login successful, welcome", user["name"])
                msg = "Success"
                break
        if msg == "failed":
            count += 1
            if count < 3:
                print("Username or password is incorrect! Please log in again.", count)
            else:
                print("User is locked!")
                break
        else:
            break
    return msg


            

# Run the program
if __name__ == "__main__":
    main()
