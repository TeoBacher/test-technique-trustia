import unittest
from exercice_3 import Menu, Food, Category


class TestRestaurant(unittest.TestCase):
    def setUp(self):
        self.menu = Menu()
        self.steak = Food("Steak Frites", 15, Category.MAIN, is_available=True)
        self.soup = Food("Soupe du jour", 6, Category.STARTER, is_available=False)
        self.menu.add_item(self.steak)
        self.menu.add_item(self.soup)

    def test_lowercase_formatting(self):
        # Checks if __str__ forces lowercase
        self.assertIn("steak frites", str(self.steak))

    def test_availability_filter(self):
        # Only available items should be "visible"
        visible = [i for i in self.menu.items if i.is_available]
        self.assertEqual(len(visible), 1)
        self.assertEqual(visible[0].name, "Steak Frites")

    def test_price_update(self):
        self.menu.update_price("Steak Frites", 20)
        self.assertEqual(self.steak.price, 20)

if __name__ == "__main__":
    unittest.main()