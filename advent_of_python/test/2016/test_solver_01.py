from unittest import TestCase

from solvers_2016.solver_01 import SolverImpl


class TestTransformer01(TestCase):
    sut: SolverImpl
    @classmethod
    def setUpClass(cls):
        cls.sut = SolverImpl()

    def test_transform_1(self):
        self.assertEqual(5, self.sut.solve_part_1("R2, L3"))
        self.assertEqual(2, self.sut.solve_part_1("R2, R2, R2"))
        self.assertEqual(12, self.sut.solve_part_1("R5, L5, R5, R3 "))

    def test_transform_2(self):
        self.assertEqual(4, self.sut.solve_part_2("R8, R4, R4, R8,"))
