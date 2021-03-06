import unittest
from .day18 import evaluer


class EvaluationTests(unittest.TestCase):

    def test_calcul_simple(self):
        self.assertEqual(evaluer("3 + 5 * 2"), "16")

    def test_autre_calcul(self):
        self.assertEqual(evaluer("12 + 4 + 5 * 10 * 3 + 2 * 4"), "2528")

    def test_parenthese(self):
        self.assertEqual(evaluer("3 + (4 * 3)"), "15")

    def test_autre_parenthese(self):
        self.assertEqual(evaluer("3 + (4 * 3) + (12 * 3) * 4"), "204")

    def test_parenthese_imbriquee(self):
        self.assertEqual(evaluer("2 * ((5 + 2) * 4) + 7"), "63")

    def test_autre_imbriquee(self):
        self.assertEqual(evaluer("2 + (4 + 3 * 7 * 8) * ((6 * 3 + 4 + 6) + 8 + 2 + 4 * 5)"), "82740")


if __name__ == '__main__':
    unittest.main()