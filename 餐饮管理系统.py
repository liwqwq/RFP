# 用户数据
user1 = {"用户名": "111", "密码": "123", "姓名": "管理员1"}
user2 = {"用户名": "222", "密码": "123", "姓名": "管理员2"}
userlist = [user1, user2]

# 商品数据
commodity1 = {"编号": "1001", "名称": "排骨", "价格": 8, "折扣": 1}
commodity2 = {"编号": "1002", "名称": "炒饭", "价格": 6, "折扣": 1}
commodity3 = {"编号": "1003", "名称": "汤", "价格": 5, "折扣": 1}
commoditylist = [commodity1, commodity2, commodity3]

# 订单数据
order1 = {
    "订单编号": "001",
    "用户名": "111",
    "商品列表": [{"编号": "1001", "数量": 2}, {"编号": "1002", "数量": 1}],
    "总价": 22.0,
    "订单状态": "已下单"
}

order2 = {
    "订单编号": "002",
    "用户名": "222",
    "商品列表": [{"编号": "1003", "数量": 3}],
    "总价": 15.0,
    "订单状态": "已配送"
}

orderlist = [order1, order2]

# 登录
def login():
    msg = "失败"
    count = 0
    while True:
        uname = input("请输入账号：")
        upwd = input("请输入密码：")
        for user in userlist:
            if uname == user["用户名"] and upwd == user["密码"]:
                print("登录成功，欢迎你", user["姓名"])
                msg = "成功"
                break
        if msg == "失败":
            count += 1
            if count < 3:
                print("用户名密码错误！请重新登录", "输入第", count, "次")
            else:
                print("用户已锁定！")
                break
        else:
            break
    return msg

# 1、显示商品列表
def showProduct():
    print("----------产品信息----------")
    print("-编号----名称----价格----折扣-")
    for commodity in commoditylist:
        print("-" + commodity["编号"] + "----" + commodity["名称"] + "-----" + str(commodity["价格"]) + "-----" + str(
            commodity["折扣"]))
    print("----------------------------")

# 2、增加商品信息
def addProduct():
    list1 = []
    for num in commoditylist:
        list1.append(int(num["编号"]))
    num = str(max(list1) + 1)
    print("----------添加商品信息----------")
    mc = input("请输入产品名称:")
    jg = float(input("请输入产品价格:"))
    zk = 1
    newProduct = {"编号": num, "名称": mc, "价格": jg, "折扣": zk}
    commoditylist.append(newProduct)
    print("商品" + mc + "添加成功")
    print("-------------------------------")
    showProduct()

# 3、删除商品
def delproduct():
    showProduct()
    while True:
        msg = 0
        num = input("请输入要删除商品的编号")
        for product in commoditylist:
            if num == product["编号"]:
                print("商品", product["名称"], "正在删除")
                commoditylist.remove(product)
                print("删除成功！")
                msg = 1
                break
        if msg == 0:
            print("输入的产品编号不正确,请重新输入")
            jx = input("取消输入请按1，继续请按2")
            if jx == "1":
                break
            elif jx == "2":
                continue
            else:
                print("输入错误请重新输入")
        else:
            showProduct()
            break

# 4、设置商品折扣
def setDiscount():
    while True:
        mag = 0
        name = input("请输入要设置折扣的商品名称")
        for x in commoditylist:
            if name == x["名称"]:
                zk = float(input("请输入要设置产品的折扣(0.1-1)"))
                x["折扣"] = zk
                print(x["名称"] + "的折扣为：" + str(zk))
                mag = 1
                break
        if mag == 0:
            print("输入的商品名称不存在，请重新输入")
            jx = input("取消输入请按1，继续请按2")
            if jx == "1":
                break
            elif jx == "2":
                continue
            else:
                print("输入错误请重新输入")
        else:
            showProduct()
            break

# 5、修改商品价格信息
def setPrice():
    while True:
        mag = 0
        num = input("请输入要设置价格的商品编号")
        for x in commoditylist:
            if num == x["编号"]:
                jg = float(input("请输入要设置产品价格"))
                x["价格"] = jg
                print(x["名称"] + "的价格为：" + str(jg))
                mag = 1
                break
        if mag == 0:
            print("输入的商品编号不存在，请重新输入")
            jx = input("取消输入请按1，继续请按2")
            if jx == "1":
                break
            elif jx == "2":
                continue
            else:
                print("输入错误请重新输入")
        else:
            showProduct()
            break

# 6、根据价格排序显示商品列表
def sort():
    choice = int(input("请选择升序或者降序（1、升序 2、降序）"))
    clist = []
    for commodity in commoditylist:
        clist.append(commodity["价格"])
    clist = list(set(clist))
    if choice == 1:
        newlist = sorted(clist)
        for price in newlist:
            for product in commoditylist:
                if price == product["价格"]:
                    print("-" + product["编号"] + "----" + product["名称"] + "-----" + str(product["价格"]) + "-----" + str(
                        product["折扣"]))
    else:
        newlist = sorted(clist, reverse=True)
        for price in newlist:
            for product in commoditylist:
                if price == product["价格"]:
                    print("-" + product["编号"] + "----" + product["名称"] + "-----" + str(product["价格"]) + "-----" + str(
                        product["折扣"]))

# 7、创建新订单
def createOrder():
    showProduct()
    order_items = []
    total_price = 0.0

    while True:
        product_id = input("请输入要购买的商品编号（输入0结束）：")
        if product_id == "0":
            break
        quantity = int(input("请输入购买数量："))

        for product in commoditylist:
            if product["编号"] == product_id:
                item_price = product["价格"] * product["折扣"] * quantity
                total_price += item_price
                order_items.append({"编号": product_id, "数量": quantity})
                print(f"已添加 {product['名称']} x {quantity} 到订单中，总价：{item_price}")
                break
        else:
            print("商品编号不存在，请重新输入。")

    if order_items:
        order_id = str(len(orderlist) + 1).zfill(3)  # 生成订单编号
        new_order = {
            "订单编号": order_id,
            "用户名": "111",  # 假设当前用户是 "111"，你可以根据实际情况修改
            "商品列表": order_items,
            "总价": total_price,
            "订单状态": "已下单"
        }
        orderlist.append(new_order)
        print(f"订单创建成功！订单编号：{order_id}，总价：{total_price}")
    else:
        print("订单为空，未创建订单。")

# 8、查看订单列表
def showOrders():
    print("----------订单信息----------")
    print("-订单编号----用户名----总价----订单状态-")
    for order in orderlist:
        print(f"-{order['订单编号']}----{order['用户名']}----{order['总价']}----{order['订单状态']}")
    print("----------------------------")

# 9、查看订单详情
def showOrderDetails():
    order_id = input("请输入要查看的订单编号：")
    for order in orderlist:
        if order["订单编号"] == order_id:
            print("----------订单详情----------")
            print(f"订单编号：{order['订单编号']}")
            print(f"用户名：{order['用户名']}")
            print(f"总价：{order['总价']}")
            print(f"订单状态：{order['订单状态']}")
            print("商品列表：")
            for item in order["商品列表"]:
                for product in commoditylist:
                    if product["编号"] == item["编号"]:
                        print(f"  {product['名称']} x {item['数量']}")
                        break
            print("----------------------------")
            return
    print("订单编号不存在，请重新输入。")

# 主程序开始
while True:
    result = login()
    if result == "成功":
        while True:
            print("*********主菜单*********")
            print("1、显示商品列表")
            print("2、增加商品信息")
            print("3、删除商品")
            print("4、设置商品折扣")
            print("5、修改商品信息")
            print("6、根据价格排序商品")
            print("7、创建新订单")
            print("8、查看订单列表")
            print("9、查看订单详情")
            print("10、退出")
            print("*********************")
            choice = int(input("请输入您的选项（1-10）"))
            if choice == 1:
                showProduct()
            elif choice == 2:
                addProduct()
            elif choice == 3:
                delproduct()
            elif choice == 4:
                setDiscount()
            elif choice == 5:
                setPrice()
            elif choice == 6:
                sort()
            elif choice == 7:
                createOrder()
            elif choice == 8:
                showOrders()
            elif choice == 9:
                showOrderDetails()
            elif choice == 10:
                print("------------系统已退出")
                break
            else:
                print("没有此功能请重新输入")
                continue