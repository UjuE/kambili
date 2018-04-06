import datasource

class Kambili:
    def __init__(self, data_source):
        self.data_source = data_source

    def generate_week_menu(self):
        return WeekMenu(self.data_source.get_menu_plans())

class WeekMenu:
    def __init__(self, menu_plans):
        self.menu_plans = menu_plans

    def get(self, day, menu_type):
        return next(meal_plan for meal_plan in self.menu_plans if meal_plan.menu_type is menu_type)

class MenuPlan:
    def __init__(self, menu_type, meal_name):
        self.menu_type = menu_type
        self.meal_name = meal_name

    def get_menu_type(self):
        return self.menu_type

    def get_meal_name(self):
        return self.meal_name