import os
import unittest

from libs.datasource import MenuDataSource
from libs.datastore import MenuDataStore


class DatasourceTest(unittest.TestCase):
    def setUp(self):
        self.neo4j_username = os.getenv('NEO_4J_USERNAME', 'Not found')
        self.neo4j_password = os.getenv('NEO_4J_PASSWORD', 'Not found')
        self.neo4j_url = os.getenv('NEO_4J_URL', 'Not found')
        self.neo4j_port = os.getenv('NEO_4J_BOLT_PORT', 'Not found')
        store = MenuDataStore(self.neo4j_url, self.neo4j_port, self.neo4j_username, self.neo4j_password)
        store.connect(store.save_meal("Garri with assorted meat banga soup"), store.save_meal_type("Lunch", "Afternoon meal"))

    def test_retrieve_data(self):

        menu_plans = MenuDataSource(self.neo4j_url, self.neo4j_port, self.neo4j_username, self.neo4j_password).get_menu_plans()
        self.assertGreaterEqual(len(menu_plans), 1)



if __name__ == '__main__':
    unittest.main()