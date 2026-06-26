
class Product:
    """
    Represents a standard physical product in the store inventory.
    Manages the core attributes of an item including its name, price,
    available stock quantity, active status, and any active promotional offer.
    """
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True


    def get_quantity(self):
        """
        Get the current stock level of the product.
        Returns:
            int: The current available quantity.
        """
        return self.quantity


    def set_quantity(self, quantity):
        """
                Update the stock quantity of the product.
                Automatically deactivates the product if the stock level hits zero.
        """
        if quantity < 0:
            raise ValueError("Product quantity can't be negative")

        self.quantity = quantity

        if self.get_quantity() == 0:
            self.active = False


    def is_active(self):
        """
          Check if the product is currently available for purchase.
          Returns:
              bool: True if the product is active, False otherwise.
          """
        if self.active:
            return True

        return False


    def activate(self):
        """Change the product's status to active."""
        self.active = True


    def deactivate(self):
        """Change the product's status to inactive."""
        self.active = False


    def show(self):
        """Print the primary details of the product."""
        print(f"{self.name}, {self.price}, {self.quantity}")


    def buy(self, quantity):
        """
               Process a purchase for a specific quantity of the product.
               Reduces stock and calculates the final total price.
               Args:
                   quantity (int): The number of items to purchase. Must be positive.
               Returns:
                   float: The calculated total price for this purchase.
               Raises:
                   ValueError: If quantity is negative or exceeds available stock.
        """

        total = 0.0
        if quantity < 0:
            raise ValueError("Product Quantity can't be negative")

        if quantity <= self.get_quantity():
            total += quantity * self.price
            self.set_quantity((self.get_quantity() - quantity))

        else:
            raise ValueError("Error! Quantity is too large")

        return total
