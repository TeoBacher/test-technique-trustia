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

class Menu:
    def __init__(self):
        self.items = []

    def add_item(self, food_item):
        self.items.append(food_item)

    def display(self):
        print("--- RESTAURANT MENU ---")
        for cat in Category:
            # Filter only available items
            visible_items = [
                item for item in self.items 
                if item.category == cat and item.is_available
            ]
            
            if visible_items:
                print(f"\n{cat.value.upper()}")
                print("-" * len(cat.value))
                for item in visible_items:
                    print(item)
    
    def find_item(self, name):
        """Finds a food object by its name (case insensitive)."""
        return next((i for i in self.items if i.name.lower() == name.lower()), None)

    def remove_item(self, name):
        """Deletes an item from the menu."""
        self.items = [i for i in self.items if i.name.lower() != name.lower()]

    def update_price(self, name, new_price):
        item = self.find_item(name)
        if item:
            item.price = new_price

    def set_availability(self, name, status: bool):
        item = self.find_item(name)
        if item:
            item.is_available = status