from store import Store
import products
import sys


product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                products.Product("Google Pixel 7", price=500, quantity=250)
                ]

best_buy = Store(product_list)


def show_all_products(best_buy):

    products_to_list = best_buy.get_all_products()

    print("\n-----------------")
    for index, product in enumerate(products_to_list, start=1):
        print(f"{index}. ", end="")
        product.show()
    print("-----------------")


def get_total_quantity(best_buy):
    total = best_buy.get_total_quantity()
    print(f"\nTotal quantity in store: {total}")


def make_order(best_buy):
    show_all_products(best_buy)
    order_list = []
    available_products = best_buy.get_all_products()
    print("\nPress 'Enter' twice to finish order process.")
    while True:
        user_ordered_input = input("Which product # do you want to buy? ")

        if user_ordered_input:
            try:
                if int(user_ordered_input) in range(1, len(available_products) + 1):
                    chosen_product = available_products[int(user_ordered_input) - 1]

                else:
                    print("Please enter a valid number! ")
                    continue

            except ValueError as e:
                print("Please enter a valid number!", e)
                continue

        quantity_of_user_item = input("What amount do you want? ")
        if quantity_of_user_item:
            try:
                if int(quantity_of_user_item) > 0:
                    order = tuple((chosen_product, int(quantity_of_user_item)))
                    order_list.append(order)
                    print("Product added to list!")

                else:
                    print("Please enter a valid (positive) amount!")

            except ValueError as ev:
                print("Please enter a valid (positive) amount #!", ev)

        if not user_ordered_input and not quantity_of_user_item:
            break

    print(f"********\nOrder made! Total payment: ${best_buy.order(order_list)}\n")


def end_program(_):
    sys.exit()


def start(best_buy):
    actions = {"1" : ["List all products in store", show_all_products],
               "2" : ["Show total amount in store", get_total_quantity],
               "3" : ["Make an order", make_order],
               "4" : ["Quit", end_program]}

    while True:
        print("\nStore menu")
        print(10 * "-")
        for number, action in actions.items():
            print(f"{number}. {action[0]}")

        user_input = input("Please select an action: ")
        actions[user_input][1](best_buy)


if __name__ == '__main__':
    start(best_buy)