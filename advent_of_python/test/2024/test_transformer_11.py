from unittest import TestCase

from solvers_2024.solver_11 import SolverImpl


class TestTransformer01(TestCase):
    sut: SolverImpl
    data: str

    @classmethod
    def setUpClass(cls):
        cls.sut = SolverImpl()
        cls.data = """
        """

    def test_transform_1(self):
        # act assert
        self.assertEqual(55312, self.sut.solve_part_1("""125 17"""))

    def test_blink(self):
        # act assert
        self.assertEqual(7, self.sut.blink("""0 1 10 99 999""", 1))
        self.assertEqual(3, self.sut.blink("""125 17""", 1))
        self.assertEqual(4, self.sut.blink("""125 17""", 2))
        self.assertEqual(5, self.sut.blink("""125 17""", 3))
        self.assertEqual(9, self.sut.blink("""125 17""", 4))
        self.assertEqual(13, self.sut.blink("""125 17""", 5))
        self.assertEqual(22, self.sut.blink("""125 17""", 6))
        self.assertEqual(55312, self.sut.blink("""125 17""", 25))
