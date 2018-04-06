import unittest

from libs.kambili import Kambili
from libs.kambili import MenuPlan
from unittest.mock import MagicMock
from libs.datasource import MenuDataSource

class KambiliTest(unittest.TestCase):
    def setUp(self):
        self.datasource = MenuDataSource()
        self.datasource.get_menu_plans = MagicMock(return_value=[MenuPlan("Breakfast", "Salmon and Spinach Omlette")])
        self.kambili = Kambili(self.datasource)


    def test_sample(self):
        week_menu = self.kambili.generate_week_menu()
        self.assertEqual(week_menu.get("Monday","Breakfast").get_meal_name(),
                         "Salmon and Spinach Omlette")

if __name__ == '__main__':
    unittest.main()