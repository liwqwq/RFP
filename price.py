# Sample commodity list for demonstration
commoditylist = [
    {"id": "001", "name": "Apple", "price": 3.0, "discount": 1.0},
    {"id": "002", "name": "Banana", "price": 1.0, "discount": 1.0},
    {"id": "003", "name": "Cherry", "price": 2.5, "discount": 1.0}
]

# Function to display the product list
def showProduct():
    print("Product List:")
    for item in commoditylist:
        print(f"- {item['id']} ---- {item['name']} ----- Price: {item['price']} ----- Discount: {item['discount']}")

# 4. Set product discount
def setDiscount():
    while True:
        name = input("Please enter the name of the product to set the discount: ")
        mag = 0
        
        for x in commoditylist:
            if name.lower() == x["name"].lower():  # case-insensitive match
                while True:
                    try:
                        zk = float(input("Please enter the discount to set for the product (0.1-1): "))
                        if 0.1 <= zk <= 1.0:
                            x["discount"] = zk
                            print(f"{x['name']}'s discount is set to: {zk}")
                            mag = 1
                            break
                        else:
                            print("Discount must be between 0.1 and 1.0. Please try again.")
                    except ValueError:
                        print("Invalid input. Please enter a valid number.")

                break
        
        if mag == 0:
            print("The product name entered does not exist, please try again.")
            jx = input("Press 1 to cancel, press 2 to continue: ")
            if jx == "1":
                break
            elif jx == "2":
                continue
            else:
                print("Input error, please try again.")
        else:
            showProduct()
            break

# 5. Modify product price information
def setPrice():
    while True:
        num = input("Please enter the ID of the product to set the price: ")
        mag = 0
        
        for x in commoditylist:
            if num == x["id"]:
                while True:
                    try:
                        jg = float(input("Please enter the price to set for the product: "))
                        if jg >= 0:
                            x["price"] = jg
                            print(f"{x['name']}'s price is set to: {jg}")
                            mag = 1
                            break
                        else:
                            print("Price cannot be negative. Please enter a valid price.")
                    except ValueError:
                        print("Invalid input. Please enter a valid number.")
                
                break
        
        if mag == 0:
            print("The product ID entered does not exist, please try again.")
            jx = input("Press 1 to cancel, press 2 to continue: ")
            if jx == "1":
                break
            elif jx == "2":
                continue
            else:
                print("Input error, please try again.")
        else:
            showProduct()
            break

# 6. Sort and display product list by price
def sortProducts():
    while True:
        try:
            choice = int(input("Please choose ascending or descending (1: Ascending 2: Descending): "))
            if choice in [1, 2]:
                break
            else:
                print("Invalid choice. Please enter 1 for Ascending or 2 for Descending.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    clist = sorted(commoditylist, key=lambda x: x["price"], reverse=(choice==2))
    
    print("Sorted Product List:")
    for product in clist:
        print(f"- {product['id']} ---- {product['name']} ----- Price: {product['price']} ----- Discount: {product['discount']}")

# Main menu for the program
def mainMenu():
    while True:
        print("\nMain Menu:")
        print("1. Set Product Discount")
        print("2. Set Product Price")
        print("3. Sort and Display Products by Price")
        print("4. Exit")
        
        choice = input("Please enter your choice: ")
        
        if choice == "1":
            setDiscount()
        elif choice == "2":
            setPrice()
        elif choice == "3":
            sortProducts()
        elif choice == "4":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
mainMenu()