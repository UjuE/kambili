import unittest
from unittest.mock import MagicMock

from libs.datasource import MenuDataSource
from libs.kamrie import Kamrie
from libs.menutypes import MenuPlan


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
        self.datasource.get_meal_types = \
            MagicMock(return_value=[
                "Breakfast", "Lunch", "Dinner"
            ])
        self.kamrie = Kamrie(self.datasource)

    def test_all_days_must_have_menu_plans(self):
        week_menu = self.kamrie.generate_week_menu()

        self.assertIsNotNone(week_menu.get("Monday"), "Week Menu must have entry for Monday")
        self.assertIsNotNone(week_menu.get("Tuesday"), "Week Menu must have entry for Tuesday")
        self.assertIsNotNone(week_menu.get("Wednesday"), "Week Menu must have entry for Wednesday")
        self.assertIsNotNone(week_menu.get("Thursday"), "Week Menu must have entry for Thursday")
        self.assertIsNotNone(week_menu.get("Friday"), "Week Menu must have entry for Friday")
        self.assertIsNotNone(week_menu.get("Saturday"), "Week Menu must have entry for Saturday")
        self.assertIsNotNone(week_menu.get("Sunday"), "Week Menu must have entry for Sunday")

    def test_monday_contains_only_one_of_each_meal_type(self):
        week_menu = self.kamrie.generate_week_menu()

        monday_menu = week_menu.get("Monday")
        self.assertEqual(len(self.get_meals_with_menu_type("Breakfast", monday_menu)), 1)
        self.assertEqual(len(self.get_meals_with_menu_type("Lunch", monday_menu)), 1)
        self.assertEqual(len(self.get_meals_with_menu_type("Dinner", monday_menu)), 1)

    def get_meals_with_menu_type(self, menu_type, day_menu):
        return [menu for menu in day_menu.menu_plans if menu.menu_type == menu_type]


if __name__ == '__main__':
    unittest.main()
