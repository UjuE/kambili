import unittest

from libs.kambili import Kambili

class KambiliTest(unittest.TestCase):
    def setUp(self):
        self.kambili = Kambili()

    def test_sample(self):
        menu_plan = self.kambili.generate_menu()
        self.assertEqual(menu_plan[0].menu_type, "Breakfast")

if __name__ == '__main__':
    unittest.main()