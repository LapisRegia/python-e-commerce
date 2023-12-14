class users:
    username = ""
    password = ""
    userID = 1

    def auto_increment(self):
        self.userID += 1

    def login(self):
        pass

    def register(self):
        pass


class customer(users):
    customer_list = [
        {"id": 1, "username": "John", "password": "112358", "address": "UNIMAS, Kota Samarahan"},
        {"id": 2, "username": "Dude", "password": "246810", "address": "UNIMAS, Kota Samarahan"}
    ]
    address = ""
    users.userID = 2

    def login(self):

        while True:
            login_prompt = "\nDo you have an existing account?" \
                            "\n0.Exit" \
                            "\n1.yes" \
                            "\n2.no" \
                            "\n--->"

            have_account = input(login_prompt)
            try:
                have_account = int(have_account)
            except ValueError:
                print("\nEnter a number!")
                continue

            match have_account:
                case 0:
                    break
                case 1:
                    print("\nLogging in as: Customer.")

                    while True:
                        login_check = 0
                        enterName = "Enter your username: "
                        self.username = input(enterName)

                        enterPass = "Enter your password: "
                        self.password = input(enterPass)

                        for cust_item in self.customer_list:
                            if cust_item["username"] == self.username:
                                login_check += 1
                                if cust_item["password"] == self.password:
                                    login_check += 1
                                    break

                        if login_check == 2:
                            print("\nLogin Successful")
                            cart_instance.shop()
                        else:
                            print("\nInvalid Name or Password!")
                            #continue -- if you put it here there isnt a way for the user to escape the loop

                        break
                case 2:
                    register_prompt = "Choose your options:" \
                               "\n1.Register" \
                               "\n2.Exit" \
                               "\n--->"
                    no_account = input(register_prompt)
                    try:
                        no_account = int(no_account)
                    except ValueError:
                        print("\nEnter a number!")
                        continue

                    match no_account:
                        case 1:
                            self.register()
                            continue
                        case 2:
                            print("\nSee you later")
                            return
                        case _:
                            print("Invalid input! please enter again!")
                            continue
                case _:
                    print("Invalid input! please enter again!")
                    continue

    def register(self):
        while True:
            exists = False
            print("\nLogging in as: Admin.")
            enterName = "\nEnter your username: "
            self.username = input(enterName)

            enterPass = "Enter your password: "
            self.password = input(enterPass)

            enterAddress = "Enter your address: "
            self.address = input(enterAddress)

            #check if the key exists
            for cust_item in self.customer_list:
                if cust_item["username"] == self.username:
                    print("\nUser already exists, please enter again!\n")
                    exists = True

            if not exists:
                # add to list of customers
                self.auto_increment()
                self.customer_list.append(
                    {"id": self.userID, "username": self.username, "password": self.password, "address": self.address})
                print("\nAccount successfully created. Returning to main menu")
                break
            if not exists:
                # update list of customers, without incrementing the userID
                self.customer_list.append(
                    {"id": self.userID, "username": self.username, "password": self.password, "address": self.address})
                print("\nAccount successfully updated. Returning to main menu")
                break


class administrator(users):
    users.userID = 2
    administrator_list = [{"id": 1, "username": "admin123", "password": "password", "workplace": "home"},
                          {"id": 2, "username": "admin312", "password": "password123", "workplace": "UNIMAS"}]

    def login(self):
        while True:
            print("\nLogging in as: Admin.")
            login_check = 0
            enterName = "Enter your username: "
            self.username = input(enterName)

            enterPass = "Enter your password: "
            self.password = input(enterPass)

            for admin_item in self.administrator_list:
                if admin_item["username"] == self.username:
                    login_check += 1
                    if admin_item["password"] == self.password:
                        login_check += 1
                        break

            if login_check == 2:
                print("\nLogin Successful")
                self.admin_menu()
                break
            else:
                print("\nInvalid Name or Password!")
                break
                # continue -- if you put it here there isnt a way for the user to escape the loop

    def admin_menu(self):
        while True:
            print("\nWelcome, ", self.username)
            menu = "\nChoose a task:" \
                   "\n1.Create a seller" \
                   "\n2.edit a seller" \
                   "\n3.delete a seller" \
                   "\n4.View and edit orders" \
                   "\n0.Exit" \
                   "\n--->"
            option = input(menu)
            try:
                option = int(option)
            except ValueError:
                print("\nEnter a number!")
                continue

            match option:
                case 1:
                    self.create_seller()
                case 2:
                    self.edit_seller()
                case 3:
                    self.delete_seller()
                case 4:
                    self.view_and_edit_orders()
                case 0:
                    break
                case _:
                    print("Invalid input! please enter again!")
                    continue

    def create_seller(self):
        while True:
            print("\nCreating a seller")
            exists = False
            enterName = "\nEnter seller username: "
            seller_session.username = input(enterName)

            enterPass = "\nEnter seller password: "
            seller_session.password = input(enterPass)

            enterProductCount = "\nEnter seller no of products: "
            seller_productCount = input(enterProductCount)
            try:
                seller_productCount = int(seller_productCount)
            except ValueError:
                print("\nEnter a number!")
                continue

            # check if the key exists
            for seller_item in seller_session.seller_list:
                if seller_item["username"] == enterName:
                    print("\nUser already exists, please enter again!\n")
                    exists = True

            if not exists:
                # add to list of customers
                seller_session.auto_increment()
                seller_session.seller_list.append(
                    {"id": seller_session.userID, "username": seller_session.username, "password": seller_session.password,
                     "no_of_products": seller_productCount})
                print("\nAccount successfully created. Returning to main menu")
                break

    def edit_seller(self):
        seller_exists = False
        while True:
            print("\nEditing a seller")
            saved_id = 0
            index = 0
            for sellers in seller_session.seller_list:
                print(sellers)

            edit_prompt = "Enter the seller ID you wish to edit: " \
                          "\n(enter 0 if you wish to exit)" \
                          "\n--->"
            option = input(edit_prompt)

            try:
                option = int(option)
            except ValueError:
                print("\nEnter a number!")
                continue
            if option == 0:
                break
            else:
                for sellers in seller_session.seller_list:
                    if sellers["id"] == option:
                        print("\nEditing seller: ", sellers["username"], "\n")
                        saved_id = sellers["id"]
                        seller_exists = True
                        break
                    index += 1
            if not seller_exists:
                print("\nSeller ID does not exist! Please enter again.")
                continue
            else:
                seller_session.seller_list.pop(index)

            while True:
                seller_exists = False
                enterName = "Enter updated seller username: "
                seller_session.username = input(enterName)

                enterPass = "Enter updated seller password: "
                seller_session.password = input(enterPass)

                enterProductCount = "Enter updated seller no of products: "
                seller_productCount = input(enterProductCount)

                try:
                    seller_productCount = int(seller_productCount)
                except ValueError:
                    print("\nEnter a number!")
                    continue

                for seller_item in seller_session.seller_list:
                    if seller_item["username"] == self.username:
                        print("\nUser already exists, please enter again!\n")
                        seller_exists = True

                if not seller_exists:
                    seller_session.seller_list.append(
                        {"id": saved_id, "username": seller_session.username,
                         "password": seller_session.password,
                         "no_of_products": seller_productCount})
                    print("\nAccount successfully edited. Returning to main menu")
                    break

    def delete_seller(self):
        seller_exists = False
        while True:
            print("\nDeleting a seller")
            index = 0
            for sellers in seller_session.seller_list:
                print(sellers)

            edit_prompt = "Enter the seller ID you wish to delete: " \
                          "\n(enter 0 if you wish to exit)" \
                          "\n--->"
            option = input(edit_prompt)

            try:
                option = int(option)
            except ValueError:
                print("\nEnter a number!")
                continue
            if option == 0:
                break
            else:
                for sellers in seller_session.seller_list:
                    if sellers["id"] == option:
                        print("\nEditing seller: ", sellers["username"], "\n")
                        seller_exists = True
                        break
                    index += 1
            if not seller_exists:
                print("\nSeller ID does not exist! Please enter again.")
                continue
            else:
                break
        seller_session.seller_list.pop(index)
        print("Seller deleted successfully.")


    def view_and_edit_orders(self):
        order_instance.show_all_orders()
        while True:
            print("\nEditing an Order")
            for sellers in seller_session.seller_list:
                print(sellers)
            view_edit_prompt = "Enter Order ID which you want to edit:" \
                               "\n(enter 0 to exit)" \
                               "\n--->"
            option = input(view_edit_prompt)
            try:
                option = int(option)
            except ValueError:
                print("\nEnter a number!")
                continue
            if option == 0:
                print("\nReturning to Admin Menu...")
                return
            index = 0
            saved_id = saved_quantity = saved_total = 0
            saved_customer_name = saved_product_name = saved_address = ""
            exists = False

            for orders in order_instance.order_list:
                if orders["order_id"] == option:
                    saved_id = orders["order_id"]
                    saved_quantity = orders["quantity"]
                    saved_total = orders["price_per_unit"]
                    saved_customer_name = orders["customer_name"]
                    saved_product_name = orders["product_name"]
                    saved_address = orders["shipped_to"]
                    exists = True
                    break
                index += 1

            if not exists:
                print("\nProduct does not exists! please enter again.")
                continue
            else:
                order_instance.order_list.pop(index)

            while True:
                enterNewStatus = "\nEnter updated order status"
                updatedStatus = input(enterNewStatus)
                #checks if input is empty
                if not updatedStatus:
                    print("\nFill in all the fields!")
                    continue
                else:
                    break
            order_instance.order_list.append(
                {"order_id": saved_id,
                 "customer_name": saved_customer_name,
                 "shipped_to": saved_address,
                 "product_name": saved_product_name,
                 "quantity": saved_quantity,
                 "price_per_unit": saved_total,
                 "status": updatedStatus})
            print ("\nOrder ID: ", saved_id, " has been updated to ", updatedStatus)
            break



class seller(users):
    seller_list = [{"id": 1, "username": "seller123", "password": "password", "no_of_products": 1},
                  {"id": 2, "username": "seller419", "password": "protien", "no_of_products": 1}]
    users.userID = 2

    def login(self):
        while True:
            print("\nLogging in as: Seller.")
            login_check = 0
            enterName = "Enter your username: "
            self.username = input(enterName)

            enterPass = "Enter your password: "
            self.password = input(enterPass)

            for seller_item in self.seller_list:
                if seller_item["username"] == self.username:
                    login_check += 1
                    if seller_item["password"] == self.password:
                        login_check += 1
                        self.userID = seller_item["id"]
                        break

            if login_check == 2:
                print("\nLogin Successful")
                self.view_product()
                break
            else:
                print("\nInvalid Name or Password!")
                # continue -- if you put it here there isnt a way for the user to escape the loop

    def view_product(self):
        while True:
            seller_prompt = "Seller menu. Enter a number to choose an option:" \
                            "\n1.add a new product" \
                            "\n2.edit a product" \
                            "\n3.remove product" \
                            "\n0. exit" \
                            "\n--->"
            option = input(seller_prompt)
            try:
                option = int(option)
            except ValueError:
                print("\nEnter a number!")
                continue

            match option:
                case 1:
                    self.add_new_product()
                    continue
                case 2:
                    self.edit_my_product()
                    continue
                case 3:
                    self.remove_product()
                    continue
                case 0:
                    break
                case _:
                    print("Invalid input! please enter again!")
                    continue

    def add_new_product(self):

        while True:
            enterProduct = "\nEnter the product name: "
            product_instance.product_name = input(enterProduct)

            enterPrice = "\nEnter the product price: "
            product_instance.price = input(enterPrice)

            try:
                product_instance.price = int(product_instance.price)
            except ValueError:
                print("\nEnter a number!")
                continue
            break

        product_instance.auto_increment()
        product_instance.product_list.append(
            {"id": product_instance.product_id,
             "seller_id": self.username,
             "product_name": product_instance.product_name,
             "price_per_unit": product_instance.price})

    def edit_my_product(self):
        index = 0
        print ("my products:\n")
        for products in product_instance.product_list:
            if products['seller_name'] == self.username:
                print(index + 1,". Product Name:", products["product_name"], " Price: ", products["price_per_unit"])
                print("\n")
                index += 1
        while True:
            edit_prompt = "Enter the product name you want to edit: " \
                          "\n(enter 0 to exit)" \
                          "\n--->"
            choose = input(edit_prompt)
            if choose == 0:
                print("returning...")
                return

            saved_id = 0
            exists = False
            for products in product_instance.product_list:
                if products["seller_name"] == customer_session.username:
                    if products["product_name"] == choose:
                        exists = True
                        saved_id = products["id"]
                index += 1

            if not exists:
                print("\nProduct does not exists! please enter again.")
                continue
            else:
                product_instance.product_list.pop(index)

            while True:
                product_name_exists = False

                enterProductName = "\nEnter your updated Product name: "
                newName = input(enterProductName)

                enterNewPrice = "\nEnter your updated stock: "
                newPrice = input(enterNewPrice)

                try:
                    newPrice = int(newPrice)
                except ValueError:
                    print("\nEnter a number!")
                    continue

                for products in product_instance.product_list:
                    if products["product_name"] == newName:
                        print("\nProduct Name already exists, please enter again!\n")
                        product_name_exists = True

                if not product_name_exists:
                    product_instance.product_list.append(
                        {"id": saved_id, "seller_name": customer_session.username, "product_name": newName,
                         "price_per_unit": newPrice}
                    )
                    print ("\nYour product : ", newName, " with price RM:", newPrice, " .00 has been updated")

    def remove_product(self):
        print("My products:\n")
        for products in product_instance.product_list:
            if products["seller_name"] == self.username:
                print("Product ID: ",products['id'], ". Product Name:", products['product_name'], " Price: RM",
                      products['price_per_unit'], ".00")
                print("\n")

        while True:
            edit_prompt = "Enter the product ID you want to edit:" \
                          "\n(enter 0 to exit)" \
                          "\n--->"
            choose = input(edit_prompt)
            try:
                choose = int(choose)
            except ValueError:
                print("Invalid input! please enter again!")
                continue
            if choose == 0:
                print("\nreturning to menu...")
                break

            index = 0
            saved_name = ""
            exists = False

            for products in product_instance.product_list:
                if products["seller_name"] == self.username:
                    if products["id"] == choose:
                        exists = True
                        saved_name = products["product_name"]
                        break
                index += 1

            if not exists:
                print("\nNothing to delete! Returning to Seller Menu")
                continue
            else:
                product_instance.product_list.pop(index)
                print("\nProduct name: ", saved_name, " has been removed.")
                product_instance.auto_decrement()
                break
