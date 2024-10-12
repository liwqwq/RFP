# Sample initial product list
commoditylist = [
    {"id": "1", "name": "Product A", "price": 10.0, "discount": 1},
    {"id": "2", "name": "Product B", "price": 15.0, "discount": 1},
]

# 1. Show product list
def showProduct():
    print("---------- Product Information ----------")
    print("-ID----Name----Price----Discount-")
    for commodity in commoditylist:
        print(f"-{commodity['id']}----{commodity['name']}-----{commodity['price']}-----{commodity['discount']}")
    print("----------------------------------------")

# 2. Add product information
def addProduct():
    list1 = []
    for num in commoditylist:
        list1.append(int(num["id"]))
    new_id = str(max(list1) + 1) if list1 else "1"  # Start with ID 1 if list is empty
    print("---------- Add Product Information ----------")
    mc = input("Please enter the product name: ")
    jg = float(input("Please enter the product price: "))
    zk = 1  # Assuming default discount is 1 (no discount)
    newProduct = {"id": new_id, "name": mc, "price": jg, "discount": zk}
    commoditylist.append(newProduct)
    print(f"Product '{mc}' added successfully")
    print("-----------------------------------------------")
    showProduct()

# 3. Delete product
def delproduct():
    showProduct()
    while True:
        num = input("Please enter the ID of the product to delete: ")
        for product in commoditylist:
            if num == product["id"]:
                print(f"Product '{product['name']}' is being deleted")
                commoditylist.remove(product)
                print("Deleted successfully!")
                return
        print("The product ID entered is incorrect, please try again")
        jx = input("Press 1 to cancel, press 2 to continue: ")
        if jx == "1":
            break
        elif jx == "2":
            continue
        else:
            print("Input error, please try again")

# 4. Main menu to run the program
def mainMenu():
    while True:
        print("\n---------- Main Menu ----------")
        print("1. Show Product List")
        print("2. Add Product")
        print("3. Delete Product")
        print("4. Exit")
        choice = input("Please select an option (1-4): ")
        
        if choice == '1':
            showProduct()
        elif choice == '2':
            addProduct()
        elif choice == '3':
            delproduct()
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

# Run the main menu
if __name__ == "__main__":
    mainMenu()