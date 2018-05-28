import unittest

from libs.kambili import Kambili
from libs.menutypes import MenuPlan
from unittest.mock import MagicMock
from libs.datasource import MenuDataSource


class KambiliTest(unittest.TestCase):
    def setUp(self):
        self.datasource = MenuDataSource("", "", "", "")
        self.datasource.get_menu_plans = \
            MagicMock(return_value=[
                MenuPlan("Breakfast", "Salmon and Spinach Omlette"),
                MenuPlan("Breakfast", "Boiled Eggs and Tuna"),
                MenuPlan("Breakfast", "Egg Stew and Fried Plantain"),
                MenuPlan("Lunch", "Grilled Chicken and Beans with Plantain Porridge"),
                MenuPlan("Lunch", "Grilled Chicken and Salad"),
                MenuPlan("Lunch", "Assorted Meat Afang Soup and Moi moi"),
                MenuPlan("Dinner", "Assorted Meat Stew and Moi moi"),
                MenuPlan("Dinner", "Assorted Meat Stew Soup and Bulgar Wheat"),
                MenuPlan("Dinner", "Fish pepper soup")
            ])
        self.kambili = Kambili(self.datasource)

    def test_all_days_must_have_menu_plans(self):
        week_menu = self.kambili.generate_week_menu()

        self.assertIsNotNone(week_menu.get("Monday"), "Week Menu must have entry for Monday")
        self.assertIsNotNone(week_menu.get("Tuesday"), "Week Menu must have entry for Tuesday")
        self.assertIsNotNone(week_menu.get("Wednesday"), "Week Menu must have entry for Wednesday")
        self.assertIsNotNone(week_menu.get("Thursday"), "Week Menu must have entry for Thursday")
        self.assertIsNotNone(week_menu.get("Friday"), "Week Menu must have entry for Friday")
        self.assertIsNotNone(week_menu.get("Saturday"), "Week Menu must have entry for Saturday")
        self.assertIsNotNone(week_menu.get("Sunday"), "Week Menu must have entry for Sunday")


if __name__ == '__main__':
    unittest.main()
