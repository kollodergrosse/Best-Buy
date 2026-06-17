from store import Store
import products
import sys

def end_program():
    sys.exit()


def start():
    actions = {"1" : ["List all products in store", Store.get_all_products],
               "2" : ["Show total amount in store", Store.get_total_quantity],
               "3" : ["Make an order", Store.order],
               "4" : ["Quit", end_program]}

    print("   Store menu")
    print("  ", 10 * "-")
    for number, action in actions.items():
        print(f"{number}. {action[0]}")

    user_input = input("Please select an action: ")
    actions[user_input][1]()


def main():

    product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    products.Product("Google Pixel 7", price=500, quantity=250)
                    ]
    #best_buy = Store(product_list)
    start()

if __name__ == '__main__':
    main()