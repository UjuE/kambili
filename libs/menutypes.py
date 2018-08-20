import random

from .constants import Day


class WeekMenu:
    def __init__(self, menu_plans, meal_types):
         self.week_menu = self.__create_day_menu_plans(meal_types, menu_plans)

    def get(self, day):
        return next(iter([x for x in self.week_menu if str(x.get_day()) == str(day)]), None)

    def __create_day_menu_plans(self, meal_types, menu_plans):
        days_menu_plan = []
        for name, member in Day.__members__.items():
            meal_types_lists = self.__random_menu_types(meal_types, menu_plans)

            days_menu_plan.append(
                DayMenuPlan(member,
                            meal_types_lists
                            ))

        return days_menu_plan

    @staticmethod
    def __random_menu_types(meal_types, menu_plans):
        meal_types_lists = []
        for name in meal_types:
            stuff = [item for item in menu_plans if str(item.meal_type) == str(name)]
            meal_types_lists.append(random.choice(stuff))
        return meal_types_lists


class DayMenuPlan:
    def __init__(self, day, menu_plans):
        self.day = str(day)
        self.meal_plans = menu_plans

    def get_menu_plan(self, menu_type):
        return next(meal_plan for meal_plan in self.meal_plans if str(meal_plan.meal_type) == str(menu_type))

    def get_day(self):
        return self.day

    def __str__(self):
        return str(self.day) + " -> " + ', '.join(str(menu_plan) for menu_plan in self.meal_plans)

    def __repr__(self):
        return self.__str__()


class MenuPlan:
    def __init__(self, menu_type: str, meal_name: str):
        self.meal_type = menu_type
        self.meal_name = meal_name

    def get_menu_type(self):
        return self.meal_type

    def get_meal_name(self):
        return self.meal_name

    def __str__(self):
        return str(self.meal_type) + "(" + str(self.meal_name) + ")"

    def __repr__(self):
        return self.__str__()
