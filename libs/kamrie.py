from datasource import MenuDataSource
from menutypes import WeekMenu


class Kamrie:
    def __init__(self, data_source: MenuDataSource):
        self.data_source = data_source

    def generate_week_menu(self):
        return WeekMenu(self.data_source.get_menu_plans(), self.data_source.get_meal_types())
