from neomodel import config
from datatypes import Meal_Type, Meal
from menutypes import MenuPlan


class MenuDataStore:
    def __init__(self, host, port, user, password):
        config.DATABASE_URL = 'bolt://%s:%s@%s:%s' % (user, password, host, port)

    def save_meal(self, meal_name, description=""):
        meal = Meal.nodes.get_or_none(name=meal_name)
        if meal is None:
            meal = Meal(name=meal_name, description=description).save()
        return meal

    def save_meal_type(self, meal_type_name, description=""):
        meal_type = Meal_Type.nodes.get_or_none(name=meal_type_name)
        if meal_type is None:
            meal_type = Meal_Type(name=meal_type_name, description=description).save()
        return meal_type

    def connect(self, meal, meal_type):
        meal.meal_types.connect(meal_type)

    def create(self, menu_plan: MenuPlan):
        self.connect(self.save_meal(menu_plan.get_meal_name()), self.save_meal_type(menu_plan.get_menu_type()))
