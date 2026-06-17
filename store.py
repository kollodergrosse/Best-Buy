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

