import unittest
from .day182 import evaluer


class EvaluationTests(unittest.TestCase):

    def test_calcul_simple(self):
        self.assertEqual(evaluer("1 + 2 * 3 + 4 * 5 + 6"), "231")

    def test_autre(self):
        self.assertEqual(evaluer("1 + (2 * 3) + (4 * (5 + 6))"), "51")

    def test_autre2(self):
        self.assertEqual(evaluer("2 * 3 + (4 * 5)"), "46")

    def test_autre3(self):
        self.assertEqual(evaluer("5 + (8 * 3 + 9 + 3 * 4 * 3)"), "1445")

    def test_autre4(self):
        self.assertEqual(evaluer("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))"), "669060")

    def test_autre5(self):
        self.assertEqual(evaluer("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"), "23340")


if __name__ == '__main__':
    unittest.main()