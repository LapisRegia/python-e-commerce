class Order:
    order_number = 1    #id
    price_total = 0.0
    Delivery_Status = ""         #delivered, shipping, packaging, cancelled etc.
    order_list = [{"order_id": 1, "customer_name": "John", "shipped_to": "UNIMAS, Kota Samarahan", "product_name": "book", "quantity": 1, "price_per_unit": 50, "status": "delivered"},
                  {"order_id": 1, "customer_name": "John", "shipped_to": "UNIMAS, Kota Samarahan", "product_name": "whey", "quantity": 1, "price_per_unit": 200,"status": "shipping"}]

    def auto_increment(self):
       self.order_number += 1

    def show_all_orders(self):
        for orders in order_instance.order_list:
            print(orders)

    def view_delivery_status(self, username):
        for order_items in self.order_list:
            if order_items["customer_name"] == customer_session.username:
                print("Order ID: ", order_items["order_id"],
                      " Product Name: ", order_items["product_name"],
                      " Quantity: ", order_items["quantity"],
                      " Price: ", order_items["price_per_unit"],
                      " DeliveryStatus: ", order_items["status"])