from unittest import TestCase

from solvers_2024.solver_02 import SolverImpl


class TestTransformer01(TestCase):
    sut: SolverImpl
    data: str

    @classmethod
    def setUpClass(cls):
        cls.sut = SolverImpl()
        cls.data = """
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
        """

    def test_transform_1(self):
        # act assert
        self.assertEqual(2, self.sut.solver_part_1(self.data))

    def test_transform_2(self):
        # act assert
        self.assertEqual(4, self.sut.solve_part_2(self.data))
