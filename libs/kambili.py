from libs.menutypes import WeekMenu

class Kambili:
    def __init__(self, data_source):
        self.data_source = data_source

    def generate_week_menu(self):
        return WeekMenu(self.data_source.get_menu_plans())
