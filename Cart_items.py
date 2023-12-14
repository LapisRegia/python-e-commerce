class Cart_item:
    item_name = ""
    quantity = 0
    sub_total = 0.0
    cart_item_list = [{"associated_with": "Dude", "product_name": "book", "quantity": 2, "price_per_unit": 50},
                      {"associated_with": "Dude", "product_name": "whey", "quantity": 1, "price_per_unit": 200}]

    def remove_from_cart(self):
        # initially shows the user their cart items, then asks the user to enter the product name
        saved_index = 0
        while True:
            remove_prompt = "\nEnter the product name you want to delete"
            chosen_item = input(remove_prompt)
            if not chosen_item:
                print("\nPlease dont enter an empty string!")
                continue
            elif chosen_item == 0:
                break

            found = False
            index = 0
            for cart_items in self.cart_item_list:
               if cart_items["associated_with"] == customer_session.username:
                   if cart_items["product_name"] == chosen_item:
                       self.quantity = cart_items["quantity"]
                       saved_index = index
                       found = True
                       break
               index += 1
            if not found:
                print("\nCart Item not found! Please enter again.")
                continue
            else:
                break
        self.cart_item_list.pop(saved_index)
        for cart in cart_instance.cart_list:
            if cart["cart_owner"] == customer_session.username:
                cart["no_of_items"] -= self.quantity


    def add_to_cart(self):
        product_instance.show_products()
        while True:
            add_prompt = "\nEnter the product id you want to add"
            chosen_item = input(add_prompt)
            try:
                chosen_item = int(chosen_item)
            except ValueError:
                print("Invalid input! please enter again!")
                continue
            if chosen_item == 0:
                print("\nreturning to menu...")
                break

            found = False
            for product in product_instance.product_list:
               if product["id"] == chosen_item:
                   found = True
                   self.item_name = product["product_name"]
                   self.sub_total = product["price_per_unit"]
                   break

            if not found:
                print("\nCart Item not found! Please enter again.")
                continue
            else:
                break
        while True:
            quantityPrompt = "\nEnter how much you want to add: "
            self.quantity = input(quantityPrompt)
            try:
                self.quantity = int(self.quantity)
            except ValueError:
                print("Invalid input! please enter again!")
                continue

            print("\n", self.item_name, " with quantity ", self.quantity," has been added to your cart.")
            self.cart_item_list.append({"associated_with": customer_session.username,
                                        "product_name": self.item_name,
                                        "quantity": self.quantity,
                                        "price_per_unit": self.sub_total})
            for cart in cart_instance.cart_list:
                if cart["cart_owner"] == customer_session.username:
                    cart["no_of_items"] += self.quantity
            break

    def checkout(self):
        numberOfEntries = 0
        subTotal = 0
        grandTotal = 0
        for cart_items in self.cart_item_list:
            if cart_items["associated_with"] == customer_session.username:
                subTotal = cart_items["price_per_unit"] * cart_items["quantity"]
                print(numberOfEntries + 1, ". Product Name: ", cart_items["product_name"], " Subtotal: RM", subTotal)
                grandTotal +=  subTotal
                numberOfEntries += 1
        if subTotal == 0:
            print("\nNo items in your cart! returning to menu.")
            return
        print("Total Price: RM", grandTotal)

        while True:
            proceedPrompt = "\nDo you want to proceed to payment? (Y/y - n?N): "
            proceed = input(proceedPrompt)
            if proceed == "y" or proceed == "y":
                break
            elif proceed == "n" or proceed == "N":
                print("\nreturning to menu...")
                return

        while True:
            cardPrompt = "\nEnter the 16 digits on you credit card: "
            cardNumber = input(cardPrompt)
            if len(cardNumber) > 16 or len(cardNumber) < 0:
                continue
            try:
                cardNumber = int(cardNumber)
            except:
                print("Invalid input! please enter again!")
                continue
            else:
                break
        print("\nCard accepted")
        index = 0
        while numberOfEntries != 0:
            for cart_items in self.cart_item_list:
                if cart_items["associated_with"]== customer_session.username:

                    order_instance.auto_increment()
                    order_instance.order_list.append({"order_id": order_instance.order_number,
                                                      "customer_name": customer_session.username,
                                                      "shipped_to": customer_session.address,
                                                      "product_name": cart_items["product_name"],
                                                      "quantity": cart_items["quantity"],
                                                      "price_per_unit": cart_items["price_per_unit"],
                                                      "status": "Packaging"})
                    self.cart_item_list.pop(index)
                    numberOfEntries -= 1
                    index = 0
                    break
                index += 1
        for cart in cart_instance.cart_list:
            if cart["cart_owner"] == customer_session.username:
                cart["no_of_items"] = 0
        print("\nYour order has been placed. Returning to customer menu...")