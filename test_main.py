# test_main.py

import unittest
from main import greet

class TestMain(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet(), "Hello, world!")
        self.assertEqual(greet("developer"), "Hello, developer!")

if __name__ == '__main__':
    unittest.main()