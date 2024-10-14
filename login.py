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
    # 修复后的用户列表显示功能
def display_users():
    print("Current user list:")
    for user in userlist:
        print(f"Username: {user['username']}, Name: {user['name']}, Locked: {user['locked']}, Attempts: {user['attempts']}")

# Main function to run the program
def main():
    while True:
        print("\nWelcome! Please choose an option:")
        print("1. Login")
        print("2. Display user list")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '1':
            login()  # Assuming the login function is already defined
        elif choice == '2':
            display_users()  # Display user list
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice, please select again.")


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

# Run the program
if __name__ == "__main__":
    main()
