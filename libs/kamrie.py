from .weekplandataaccess import WeekMenuDataAccess
from .menudatasource import MenuDataSource
from .menutypes import WeekMenu


class Kamrie:
    def __init__(self, data_source: MenuDataSource, week_menu_data_access: WeekMenuDataAccess):
        self.data_source = data_source
        self.week_menu_data_access = week_menu_data_access

    def generate_week_menu(self):
        return WeekMenu(self.data_source.get_menu_plans(), self.data_source.get_meal_types())

    def store_week_menu(self, user_id, week_number, week_menu):
        self.week_menu_data_access.store_week_menu(user_id, week_number, week_menu)

    def get_week_menu(self, user_id, week_number):
        return self.week_menu_data_access.get_week_menu(user_id, week_number)
