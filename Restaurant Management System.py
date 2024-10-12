# User data
user1 = {"username": "111", "password": "123", "name": "Admin 1"}
user2 = {"username": "222", "password": "123", "name": "Admin 2"}
userlist = [user1, user2]

# Product data
commodity1 = {"id": "1001", "name": "Pork Ribs", "price": 8, "discount": 1}
commodity2 = {"id": "1002", "name": "Fried Rice", "price": 6, "discount": 1}
commodity3 = {"id": "1003", "name": "Soup", "price": 5, "discount": 1}
commoditylist = [commodity1, commodity2, commodity3]

# Order data
order1 = {
    "order_id": "001",
    "username": "111",
    "product_list": [{"id": "1001", "quantity": 2}, {"id": "1002", "quantity": 1}],
    "total_price": 22.0,
    "order_status": "Ordered"
}

order2 = {
    "order_id": "002",
    "username": "222",
    "product_list": [{"id": "1003", "quantity": 3}],
    "total_price": 15.0,
    "order_status": "Delivered"
}

orderlist = [order1, order2]

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
                msg = "success"
                break
        if msg == "failed":
            count += 1
            if count < 3:
                print("Username or password is incorrect! Please log in again.", "Attempt number:", count)
            else:
                print("User is locked!")
                break
        else:
            break
    return msg

# 1. Show product list
def showProduct():
    print("----------Product Information----------")
    print("-ID----Name----Price----Discount-")
    for commodity in commoditylist:
        print("-" + commodity["id"] + "----" + commodity["name"] + "-----" + str(commodity["price"]) + "-----" + str(commodity["discount"]))
    print("----------------------------")

# 2. Add product information
def addProduct():
    list1 = []
    for num in commoditylist:
        list1.append(int(num["id"]))
    num = str(max(list1) + 1)
    print("----------Add Product Information----------")
    mc = input("Please enter the product name: ")
    jg = float(input("Please enter the product price: "))
    zk = 1
    newProduct = {"id": num, "name": mc, "price": jg, "discount": zk}
    commoditylist.append(newProduct)
    print("Product " + mc + " added successfully")
    print("-------------------------------")
    showProduct()

# 3. Delete product
def delproduct():
    showProduct()
    while True:
        msg = 0
        num = input("Please enter the ID of the product to delete: ")
        for product in commoditylist:
            if num == product["id"]:
                print("Product", product["name"], "is being deleted")
                commoditylist.remove(product)
                print("Deleted successfully!")
                msg = 1
                break
        if msg == 0:
            print("The product ID entered is incorrect, please try again")
            jx = input("Press 1 to cancel, press 2 to continue: ")
            if jx == "1":
                break
            elif jx == "2":
                continue
            else:
                print("Input error, please try again")
        else:
            showProduct()
            break

# 4. Set product discount
def setDiscount():
    while True:
        mag = 0
        name = input("Please enter the name of the product to set the discount: ")
        for x in commoditylist:
            if name == x["name"]:
                zk = float(input("Please enter the discount to set for the product (0.1-1): "))
                x["discount"] = zk
                print(x["name"] + "'s discount is: " + str(zk))
                mag = 1
                break
        if mag == 0:
            print("The product name entered does not exist, please try again")
            jx = input("Press 1 to cancel, press 2 to continue: ")
            if jx == "1":
                break
            elif jx == "2":
                continue
            else:
                print("Input error, please try again")
        else:
            showProduct()
            break

# 5. Modify product price information
def setPrice():
    while True:
        mag = 0
        num = input("Please enter the ID of the product to set the price: ")
        for x in commoditylist:
            if num == x["id"]:
                jg = float(input("Please enter the price to set for the product: "))
                x["price"] = jg
                print(x["name"] + "'s price is: " + str(jg))
                mag = 1
                break
        if mag == 0:
            print("The product ID entered does not exist, please try again")
            jx = input("Press 1 to cancel, press 2 to continue: ")
            if jx == "1":
                break
            elif jx == "2":
                continue
            else:
                print("Input error, please try again")
        else:
            showProduct()
            break

# 6. Sort and display product list by price
def sort():
    choice = int(input("Please choose ascending or descending (1: Ascending 2: Descending): "))
    clist = []
    for commodity in commoditylist:
        clist.append(commodity["price"])
    clist = list(set(clist))
    if choice == 1:
        newlist = sorted(clist)
        for price in newlist:
            for product in commoditylist:
                if price == product["price"]:
                    print("-" + product["id"] + "----" + product["name"] + "-----" + str(product["price"]) + "-----" + str(product["discount"]))
    else:
        newlist = sorted(clist, reverse=True)
        for price in newlist:
            for product in commoditylist:
                if price == product["price"]:
                    print("-" + product["id"] + "----" + product["name"] + "-----" + str(product["price"]) + "-----" + str(product["discount"]))

# 7. Create a new order
def createOrder():
    showProduct()
    order_items = []
    total_price = 0.0

    while True:
        product_id = input("Please enter the product ID to purchase (enter 0 to finish): ")
        if product_id == "0":
            break
        quantity = int(input("Please enter the quantity to purchase: "))

        for product in commoditylist:
            if product["id"] == product_id:
                item_price = product["price"] * product["discount"] * quantity
                total_price += item_price
                order_items.append({"id": product_id, "quantity": quantity})
                print(f"Added {product['name']} x {quantity} to the order, total price: {item_price}")
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
        print(f"Order created successfully! Order ID: {order_id}, Total Price: {total_price}")
    else:
        print("The order is empty, no order created.")

# 8. View order list
def showOrders():
    print("----------Order Information----------")
    print("-Order ID----Username----Total Price----Order Status-")
    for order in orderlist:
        print(f"-{order['order_id']}----{order['username']}----{order['total_price']}----{order['order_status']}")
    print("----------------------------")

# 9. View order details
def showOrderDetails():
    order_id = input("Please enter the order ID to view: ")
    for order in orderlist:
        if order["order_id"] == order_id:
            print("----------Order Details----------")
            print(f"Order ID: {order['order_id']}")
            print(f"Username: {order['username']}")
            print(f"Total Price: {order['total_price']}")
            print(f"Order Status: {order['order_status']}")
            print("Product List:")
            for item in order["product_list"]:
                for product in commoditylist:
                    if product["id"] == item["id"]:
                        print(f"  {product['name']} x {item['quantity']}")