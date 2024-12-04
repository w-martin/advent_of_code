from unittest import TestCase

from solvers_2015.solver_04 import SolverImpl


class TestTransformer04(TestCase):
    sut: SolverImpl
    @classmethod
    def setUpClass(cls):
        cls.sut = SolverImpl()

    def test_transform_1(self):
        self.assertEqual(609043, self.sut.solve_part_1("abcdef"))
        self.assertEqual(1048970, self.sut.solve_part_1("pqrstuv"))
