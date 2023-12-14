class Products:
    no_of_products = 2
    product_id = 2
    product_name = ""
    price = 0

    product_list = [{"id": 1, "seller_name": "seller123", "product_name": "book", "price_per_unit": 50},
                    {"id": 2, "seller_name": "optimum nutrition", "product_name": "whey", "price_per_unit": 200}]
    def auto_increment(self):
        #this one here is used by the seller class, manipulates the number of products in the system
        self.no_of_products += 1
        self.product_id += 1

    def auto_decrement(self):
        # used by the seller class when deleting a product
        # literally the same as above but ONLY DECREMENTING no_of_products
        # why? phpmyadmin does it so why not.
        self.no_of_products -= 1

    def show_products(self):
        print("\nShowing all available products")
        for products in self.product_list:
            print ("Product ID: ", products["id"], " Product name: ", products["product_name"], " Price: RM", products["price_per_unit"])

    def get_details(self):
        self.show_products()
        while True:
            get_details_prompt = "Enter the Product ID you wish to edit." \
                                 "\n(input 0 to exit)" \
                                 "\n--->"
            get_ID = input(get_details_prompt)
            try:
                get_ID = int(get_ID)
            except ValueError:
                print("Invalid input! please enter again!")
                continue
            if get_ID == 0:
                print("\nreturning to menu...")
                break

            found = False
            for products in self.product_list:
                if products["id"] == get_ID:
                    print("\nProduct ID found!")
                    print ("Product ID: ", products["id"],
                           " Product name: ", products["product_name"],
                           " Sold by: ", products["seller_name"],
                           "\nPrice: RM", products["price_per_unit"])
                    found = True
            if not found:
                print("\nProduct ID not found! Please enter again.")
                continue
            else:
                break