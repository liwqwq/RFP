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

# Main function to run the program
def main():
    while True:
        print("Welcome! Please choose an option:")
        print("1. Login")
        print("2. Register")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '1':
            login()
        elif choice == '2':
            register()
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice, please select again.")
# Sample user list for demonstration purposes
userlist = [
    {"username": "user1", "password": "pass1", "name": "Alice"},
    {"username": "user2", "password": "pass2", "name": "Bob"}
]

# Function to register a new user
def register():
    new_user = {}
    while True:
        new_user["username"] = input("Enter a new username: ")
        
        # Check if the username already exists
        if any(user["username"] == new_user["username"] for user in userlist):
            print("Username already exists. Please try a different one.")
        else:
            break
    
    while True:
        password = input("Enter a new password: ")
        confirm_password = input("Confirm your password: ")
        
        # Check if the passwords match
        if password != confirm_password:
            print("Passwords do not match. Please try again.")
        else:
            new_user["password"] = password
            break

    new_user["name"] = input("Enter your name: ")

    # Add the new user to the user list
    userlist.append(new_user)
    print(f"Registration successful! Welcome, {new_user['name']}. You can now log in.")
    return True

# Main function to run the program
def main():
    while True:
        print("Welcome! Please choose an option:")
        print("1. Login")
        print("2. Register")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '1':
            login()
        elif choice == '2':
            register()
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice, please select again.")
            # Sample user list for demonstration purposes
userlist = [
    {"username": "user1", "password": "pass1", "name": "Alice"},
    {"username": "user2", "password": "pass2", "name": "Bob"}
]

# Function to register a new user
def register():
    new_user = {}
    while True:
        new_user["username"] = input("Enter a new username: ")
        
        # Check if the username already exists
        if any(user["username"] == new_user["username"] for user in userlist):
            print("Username already exists. Please try a different one.")
        else:
            break
    
    while True:
        password = input("Enter a new password: ")
        confirm_password = input("Confirm your password: ")
        
        # Check if the passwords match
        if password != confirm_password:
            print("Passwords do not match. Please try again.")
        else:
            new_user["password"] = password
            break

    new_user["name"] = input("Enter your name: ")

    # Add the new user to the user list
    userlist.append(new_user)
    print(f"Registration successful! Welcome, {new_user['name']}. You can now log in.")
    return True

# Main function to run the program
def main():
    while True:
        print("Welcome! Please choose an option:")
        print("1. Login")
        print("2. Register")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '1':
            login()
        elif choice == '2':
            register()
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice, please select again.")

# Run the program
if __name__ == "__main__":
    main()


# Run the program
if __name__ == "__main__":
    main()

# Run the program
if __name__ == "__main__":
    main()
