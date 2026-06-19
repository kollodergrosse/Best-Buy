
class Product:

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True


    def get_quantity(self):
        return self.quantity


    def set_quantity(self, quantity):
        if quantity < 0:
            raise ValueError("Product quantity can't be negative")

        self.quantity = quantity

        if self.get_quantity() == 0:
            self.active = False


    def is_active(self):
        if self.active:
            return True

        return False


    def activate(self):
        self.active = True


    def deactivate(self):
        self.active = False


    def show(self):
        print(f"{self.name}, {self.price}, {self.quantity}")


    def buy(self, quantity):
        #is active
        total = 0.0
        if quantity < 0:
            raise ValueError("Product Quantity can't be negative")

        if quantity <= self.get_quantity():
            total += quantity * self.price
            self.set_quantity((self.get_quantity() - quantity))

        else:
            raise ValueError("Error! Quantity is too large")

        return total