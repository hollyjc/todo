#Test for unittest/ci/c

import unittest
from main import add_fun


class dummytest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)