import random

from libs.constants import Day, MealType


class WeekMenu:
    def __init__(self, menu_plans):
        self.day_menu_plans = self.__create_day_menu_plans(menu_plans)

    def get(self, day):
        return [x for x in self.day_menu_plans if str(x.get_day()) == str(day)][0]

    @staticmethod
    def __create_day_menu_plans(menu_plans):
        meal_types_lists = []
        for name, member in MealType.__members__.items():
            meal_types_lists.extend([item for item in menu_plans if str(item.menu_type) == str(name)])


        days_menu_plan = []
        for name, member in Day.__members__.items():
            days_menu_plan.append(
                DayMenuPlan(member,
                            list(map(lambda menu_plan: random.choice(meal_types_lists), meal_types_lists))
                            ))

        return days_menu_plan


class DayMenuPlan:
    def __init__(self, day, menu_plans):
        self.day = day
        self.menu_plans = menu_plans

    def get_menu_plan(self, menu_type):
        return next(meal_plan for meal_plan in self.menu_plans if str(meal_plan.menu_type) == str(menu_type))

    def get_day(self):
        return self.day

    def __str__(self):
        return str(self.day) + " -> " + ', '.join(str(menu_plan) for menu_plan in self.menu_plans)

    def __repr__(self):
        return self.__str__()


class MenuPlan:
    def __init__(self, menu_type: str, meal_name: str):
        self.menu_type = menu_type
        self.meal_name = meal_name

    def get_menu_type(self):
        return self.menu_type

    def get_meal_name(self):
        return self.meal_name

    def __str__(self):
        return str(self.menu_type) + "(" + str(self.meal_name) + ")"

    def __repr__(self):
        return self.__str__()
