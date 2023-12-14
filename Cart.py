class Cart:
    items_in_cart = 0
    total_quantity = 0
    total_price = 0.0

    cart_list = [{"cart_owner": "Dude", "no_of_items": 3}]

    def view_cart(self):
        for cart in self.cart_list:
            if cart["cart_owner"] == customer_session.username:
                print("\nNumber of items in cart: ",cart["no_of_items"])
        self.calc_total_prices()
        print("Total price :RM", self.total_price)

    def calc_total_prices(self):
        self.total_price = 0
        for cart_items in cart_item_instance.cart_item_list:
            if  customer_session.username.__eq__(cart_items["associated_with"]):
                self.total_price += (cart_items["price_per_unit"] * cart_items["quantity"])

    def shop(self):
        #a main menu.
        # self explanatory, just a switch function (match in c++)
        # there are loads of these in the program, so you can copy paste
        # cases:
        #   product_instance.show_products() (from products class)
        #   product_instance.get_details() (from products class)
        #   self.view_cart() (from hereon i trust you get the gist of it. USE THE CLASS INSTANCES,
        #                     DO NOT redeem CREATE A NEW CLASS OBJECT
        #   add_to_cart() (from Cart_item class)
        #   remove_from_cart() (from Cart_item class)
        #   checkout() (from Cart_item class)
        #   view_delivery_status() (from products class)
        #   case 0: break (exit)
        while True:
            shopGreetings = "\nwelcome to The Shop."
            shopPrompt = "Customer menu. Enter a number to choose an option:" \
                      "\n1.Show products" \
                      "\n2.See products in detail" \
                      "\n3.View your cart" \
                      "\n4.Add a product to cart" \
                      "\n5.Remove a product from cart" \
                      "\n6.Checkout" \
                      "\n7.View your orders" \
                      "\n0.Exit" \
                      "\n--->"
            print(shopGreetings)
            shopRequest = input(shopPrompt)

            try:
                shopRequest = int(shopRequest)
            except ValueError:
                print("\nEnter a number!")
                continue

            match shopRequest:
                case 0:
                    break
                case 1:
                    product_instance.show_products()
                    continue
                case 2:
                    product_instance.get_details()
                    continue
                case 3:
                    self.view_cart()
                    continue
                case 4:
                    cart_item_instance.add_to_cart()
                    continue
                case 5:
                    cart_item_instance.remove_from_cart()
                    continue
                case 6:
                    cart_item_instance.checkout()
                    continue
                case 7:
                    order_instance.view_delivery_status(customer_session.username)
                case _:
                    print("Invalid input! please enter again!")
                    continue
