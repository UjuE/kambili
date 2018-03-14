class Kambili:
    def generate_menu(self):
        return [MenuPlan("Breakfast")]

class MenuPlan:
    def __init__(self, menu_type):
        self.menu_type = menu_type

    def get_menu_type(self):
        return self.menu_type
