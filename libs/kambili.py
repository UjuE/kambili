import random
from .constants import Day
from .constants import MealType


class Kambili:
    def __init__(self, data_source):
        self.data_source = data_source

    def generate_week_menu(self):
        return WeekMenu(self.data_source.get_menu_plans())


class WeekMenu:
    def __init__(self, menu_plans):
        self.day_menu_plans = self.__create_day_menu_plans(menu_plans)

    def get(self, day):
        return filter(lambda x: str(x.get_day) is str(day), self.day_menu_plans)

    @staticmethod
    def __create_day_menu_plans(menu_plans):
        meal_types_lists = []
        for name, member in MealType.__members__.items():
            meal_types_lists.append(list(filter(lambda item: str(item.menu_type) is member.describe(), menu_plans)))

        days_menu_plan = []
        for name, member in Day.__members__.items():
            days_menu_plan.append(
                DayMenuPlan(member,
                            list(map(lambda menu_plan: random.choice(menu_plan), meal_types_lists))
                            ))

        return days_menu_plan


class DayMenuPlan:
    def __init__(self, day, menu_plans):
        self.day = day
        self.menu_plans = menu_plans

    def get_menu_plan(self, menu_type):
        return next(meal_plan for meal_plan in self.menu_plans if str(meal_plan.menu_type) is str(menu_type))

    def get_day(self):
        return self.day

    def __str__(self):
        return str(self.day) + " -> " + ', '.join(str(menu_plan) for menu_plan in self.menu_plans)


class MenuPlan:
    def __init__(self, menu_type, meal_name):
        self.menu_type = menu_type
        self.meal_name = meal_name

    def get_menu_type(self):
        return self.menu_type

    def get_meal_name(self):
        return self.meal_name

    def __str__(self):
        return str(self.menu_type) + "(" + str(self.meal_name) + ")"
