import unittest

from libs.Kambili import Kambili

class KambiliTest(unittest.TestCase):
    def setUp(self):
        self.kambili = Kambili()

    def test_sample(self):
        opts = self.kambili.generate_menu()
        self.assertEqual(opts, 'Hello World')

if __name__ == '__main__':
    unittest.main()