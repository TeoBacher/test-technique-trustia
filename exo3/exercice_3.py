from enum import Enum

class Category(Enum):
    STARTER = "entrées"
    MAIN = "plats"
    DESSERT = "desserts"

class Food:
    def __init__(self, name, price, category, is_available=True):
        self.name = name
        self.price = price
        self.category = category
        self.is_available = is_available

    def __str__(self):
        """Displays the name in lowercase and price with €."""
        return f"• {self.name.lower()} — {self.price}€"