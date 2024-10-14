# Sample lists for demonstration purposes
commoditylist = [
    {"id": "001", "name": "Product A", "price": 10.0, "discount": 0.9},
    {"id": "002", "name": "Product B", "price": 20.0, "discount": 1.0},
    {"id": "003", "name": "Product C", "price": 15.0, "discount": 0.8}
]

orderlist = []

# 7. Create a new order
def createOrder():
    showProduct()
    order_items = []
    total_price = 0.0

    while True:
        product_id = input("Please enter the product ID to purchase (enter 0 to finish): ")
        if product_id == "0":
            break
        quantity = input("Please enter the quantity to purchase: ")

        # Check if the quantity is a valid integer
        try:
            quantity = int(quantity)
            if quantity <= 0:
                print("Invalid quantity. Quantity should be a positive number.")
                continue
        except ValueError:
            print("Invalid input. Please enter a valid number for quantity.")
            continue

        # Find the product in the commodity list
        for product in commoditylist:
            if product["id"] == product_id:
                item_price = product["price"] * product["discount"] * quantity
                total_price += item_price
                order_items.append({"id": product_id, "quantity": quantity})
                print(f"Added {product['name']} x {quantity} to the order, total price for this item: {item_price:.2f}")
                break
        else:
            print("Product ID does not exist, please try again.")

    if order_items:
        order_id = str(len(orderlist) + 1).zfill(3)  # Generate order ID
        new_order = {
            "order_id": order_id,
            "username": "111",  # Assume current user is "111", modify as needed
            "product_list": order_items,
            "total_price": total_price,
            "order_status": "Ordered"
        }
        orderlist.append(new_order)
        print(f"Order created successfully! Order ID: {order_id}, Total Price: {total_price:.2f}")
    else:
        print("The order is empty, no order created.")

# 8. View order list
def showOrders():
    if not orderlist:
        print("No orders found.")
        return

    print("----------Order Information----------")
    print("-Order ID----Username----Total Price----Order Status-")
    for order in orderlist:
        print(f"-{order['order_id']}----{order['username']}----{order['total_price']:.2f}----{order['order_status']}")
    print("----------------------------")

# 9. View order details
def showOrderDetails():
    order_id = input("Please enter the order ID to view: ")

    # Check if the order exists
    for order in orderlist:
        if order["order_id"] == order_id:
            print("----------Order Details----------")
            print(f"Order ID: {order['order_id']}")
            print(f"Username: {order['username']}")
            print(f"Total Price: {order['total_price']:.2f}")
            print(f"Order Status: {order['order_status']}")
            print("Product List:")
            for item in order["product_list"]:
                for product in commoditylist:
                    if product["id"] == item["id"]:
                        print(f"  {product['name']} x {item['quantity']}")
                        break
            print("----------------------------")
            return

    # If order ID not found
    print("Order number does not exist, please re-enter.")

# 10. Show available products
def showProduct():
    print("----------Available Products----------")
    print("-Product ID----Product Name----Price----Discount-")
    for product in commoditylist:
        print(f"-{product['id']}----{product['name']}----{product['price']:.2f}----{product['discount'] * 100}%")
    print("----------------------------")

# Main Menu
def mainMenu():
    while True:
        print("\n----------Main Menu----------")
        print("1. Create a new order")
        print("2. View orders")
        print("3. View order details")
        print("4. Exit")
        choice = input("Please choose an option (1/2/3/4): ")

        if choice == "1":
            createOrder()
        elif choice == "2":
            showOrders()
        elif choice == "3":
            showOrderDetails()
        elif choice == "4":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

# Run the program
mainMenu()