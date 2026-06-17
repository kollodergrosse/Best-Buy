
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self):
        #Getter-Methode für die Menge. Gibt die Menge (int) zurück.
        return self.quantity

    def set_quantity(self, quantity):
        #Setter-Methode für die Menge. Wenn die Menge 0 erreicht, wird das Produkt deaktiviert.
        self.quantity = quantity
        if self.quantity == 0:
            self.active = False

    def is_active(self):
        #Getter-Methode für aktiv. Gibt True zurück, wenn das Produkt aktiv ist, andernfalls False.
        if self.active:
            return True

    def activate(self):
        self.active = True

    def deactivate(self):
        #Deaktiviert das Produkt.
        self.active = False

    def show(self):
        #Gibt einen String, der das Produkt repräsentiert, auf der Konsole aus, z.B: "MacBook Air M2, Price: 1450, Quantity: 100"
        print(f"{self.name}, {self.price}, {self.quantity}")

    def buy(self, quantity):
        #Kauft eine bestimmte Menge des Produkts. Gibt den Gesamtpreis (float) des Kaufs zurück.
        #Aktualisiert die Produktmenge.
        #Bei Problemen (wann? darüber nachdenken), wird eine Ausnahme ausgelöst.
        total_price = quantity * self.price
        self.quantity = self.quantity - quantity
        return f"{self.name}, {total_price}€, {self.quantity}"



bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
mac = Product("MacBook Air M2", price=1450, quantity=100)

print(bose.buy(50))
print(mac.buy(100))
print(mac.is_active())

bose.show()
mac.show()

bose.set_quantity(1000)
bose.show()