import products

class Store:
    products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        #Entfernt ein Produkt aus dem Store.
        pass

    def get_total_quantity(self):
        #Gibt zurück, wie viele Artikel insgesamt im Store vorhanden sind.
        return

    def get_all_products(self):
        #Gibt alle Produkte im Store zurück, die aktiv sind.
        return products

    def order(self, shopping_list):
        #Erhält eine Liste von Tupeln, wobei jedes Tupel zwei Elemente enthält:
        #Produkt (Produktklasse) und Menge (int).
        #Kauft die Produkte und gibt den Gesamtpreis der Bestellung zurück.
        article = shopping_list[0]
        quantity = shopping_list[1]
        return products.Product.buy(article, quantity)


bose = products.Product("Bose QuietComfort Earbuds", price=250, quantity=500)
mac = products.Product("MacBook Air M2", price=1450, quantity=100)

best_buy = Store([bose, mac])
price = best_buy.order([(bose, 5), (mac, 30), (bose, 10)])
print(f"Order cost: {price} dollars.")