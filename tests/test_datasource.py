from __future__ import absolute_import

import unittest
from libs.datasource import MenuDataSource


class DatasourceTest(unittest.TestCase):
    def setUp(self):
        print("Setup")

    def tearDown(self):
        print("teardown")

    @unittest.skip
    def test_retrieve_data(self):
        menuDataSource = MenuDataSource("localhost",7883, "neo4j", "password").get_menu_plans()
        self.assertEquals(len(menuDataSource), 16)



if __name__ == '__main__':
    unittest.main()