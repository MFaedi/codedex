
from coffee_menu import CoffeeMenu
import unittest

class TestCoffeeMenu(unittest.TestCase):

    def setUp(self):
        self.coffee = CoffeeMenu()
        
    def tearDown(self):
        self.coffee = None

    def test_get_price_existing_item(self):
        self.assertEqual(self.coffee.get_price('latte'), 2.75)

    def test_get_price_non_existing_item(self):
        self.assertIsNone(self.coffee.get_price('mokka'))

    def test_add_item(self):
        self.coffee.add_item('mokka', 3.00)
        self.assertEqual(self.coffee.get_price('mokka'), 3.00)

    def test_add_item_other(self):
        self.coffee.add_item_other('ice', 1.75)
        self.assertEqual(self.coffee.get_price('ice'), 1.75)


if __name__ == '__main__':
    unittest.main()