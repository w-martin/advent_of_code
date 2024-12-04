from unittest import TestCase

from solvers_2024.solver_01 import SolverImpl


class TestTransformer01(TestCase):
    sut: SolverImpl
    data: str
    @classmethod
    def setUpClass(cls):
        cls.sut = SolverImpl()
        cls.data = """
        3   4
4   3
2   5
1   3
3   9
3   3
        """

    def test_transform_1(self):
        # act assert
        self.assertEqual(11, self.sut.solve_part_1(self.data))

    def test_transform_2(self):
        # act assert
        self.assertEqual(31, self.sut.solve_part_2(self.data))
