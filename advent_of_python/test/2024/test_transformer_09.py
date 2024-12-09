from unittest import TestCase

from solvers_2024.solver_09 import SolverImpl


class TestTransformer01(TestCase):
    sut: SolverImpl
    data: str

    @classmethod
    def setUpClass(cls):
        cls.sut = SolverImpl()
        cls.data = """
2333133121414131402
        """

    def test_transform_1(self):
        # act assert
        self.assertEqual(1928, self.sut.solve_part_1(self.data))

    def test_transform_2(self):
        # act assert
        self.assertEqual(2858, self.sut.solve_part_2(self.data))
