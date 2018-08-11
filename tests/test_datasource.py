import os
import unittest

from neomodel import db, clear_neo4j_database

from libs.datasource import MenuDataSource
from libs.datastore import MenuDataStore


class DatasourceTest(unittest.TestCase):
    def setUp(self):
        self.neo4j_username = os.getenv('NEO_4J_USERNAME', 'Not found')
        self.neo4j_password = os.getenv('NEO_4J_PASSWORD', 'Not found')
        self.neo4j_url = os.getenv('NEO_4J_URL', 'Not found')
        self.neo4j_port = os.getenv('NEO_4J_BOLT_PORT', 'Not found')
        self.store = MenuDataStore(self.neo4j_url, self.neo4j_port, self.neo4j_username, self.neo4j_password)
        self.data_source = MenuDataSource(self.neo4j_url, self.neo4j_port, self.neo4j_username, self.neo4j_password)

    def tearDown(self):
        clear_neo4j_database(db)

    def test_retrieve_data(self):
        meal = self.store.save_meal("Garri with assorted meat banga soup")
        meal_type = self.store.save_meal_type("Lunch", "Afternoon meal")
        self.store.connect(meal, meal_type)

        menu_plans = self.data_source.get_menu_plans()
        self.assertGreaterEqual(len(menu_plans), 1)

    def test_retrieve_meal_types(self):
        self.store.save_meal_type("Lunch")
        self.store.save_meal_type("Breakfast")
        self.store.save_meal_type("Dinner")
        self.store.save_meal_type("Snack")

        meal_types = self.data_source.get_meal_types()

        self.assertEqual(len(meal_types), 4)


if __name__ == '__main__':
    unittest.main()
