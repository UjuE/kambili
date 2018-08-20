from pymongo import MongoClient


class WeekMenuDataAccess:
    def __init__(self, url, db_name, collection_name):
        self.client = MongoClient(url)
        self.collection = self.client[db_name][collection_name]

    def store_week_menu(self, user_id, week_number, week_menu):
        self.collection.insert_one(self.week_menu_details(user_id, week_number, week_menu))

    def get_week_menu(self, user_id, week_number):
        return self.collection.find_one({"week_number": week_number, "user_id": user_id})

    @staticmethod
    def week_menu_details(user_id, week_number, week_menu):
        return {
            'week_menu': week_menu,
            'week_number': week_number,
            'user_id': user_id
        }
