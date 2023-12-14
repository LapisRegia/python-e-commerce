from Users import *
from Products import *
from Cart import *
from Cart_items import *
from Order import *


def main():
    # section to initialize all classes
    cart_instance = Cart()
    cart_item_instance = Cart_item()
    order_instance = Order()
    product_instance = Products()
    customer_session = customer()
    administrator_session = administrator()
    seller_session = seller()

    greetings = "\nwelcome to our E-Commerce program."
    request = "\nlogin as:" \
              "\n1.Customer" \
              "\n2.Seller" \
              "\n3.Administrator" \
              "\n0.Exit" \
              "\n--->"

    while True:
        print(greetings)

        chosen = input(request)

        try:
            chosen = int(chosen)
        except ValueError:
            print("\nEnter a number!")
            continue

        match chosen:
            case 0:
                break
            case 1:
                customer_session.login()
                continue
            case 2:
                seller_session.login()
                continue
            case 3:
                administrator_session.login()
                continue
            case _:
                print("Invalid input! please enter again!")
                continue

if __name__ == "__main__":
    main()