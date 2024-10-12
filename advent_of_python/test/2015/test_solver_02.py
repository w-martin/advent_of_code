from unittest import TestCase

from solvers_2015.solver_02 import SolverImpl


class TestTransformer01(TestCase):
    sut: SolverImpl
    @classmethod
    def setUpClass(cls):
        cls.sut = SolverImpl()

    def test_transform_1(self):
        self.assertEqual(58, self.sut.solver_part_1("2x3x4"))
        self.assertEqual(43, self.sut.solver_part_1("1x1x10"))

    def test_transform_2(self):
        self.assertEqual(34, self.sut.solve_part_2("2x3x4"))
        self.assertEqual(34, self.sut.solve_part_2("4x2x3"))
        self.assertEqual(14, self.sut.solve_part_2("1x1x10"))
