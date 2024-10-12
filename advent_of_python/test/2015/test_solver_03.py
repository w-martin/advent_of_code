from unittest import TestCase

from solvers_2015.solver_03 import SolverImpl


class TestSolver03(TestCase):
    sut: SolverImpl
    @classmethod
    def setUpClass(cls):
        cls.sut = SolverImpl()

    def test_transform_1(self):
        self.assertEqual(2, self.sut.solver_part_1(">"))
        self.assertEqual(4, self.sut.solver_part_1("^>v<"))
        self.assertEqual(2, self.sut.solver_part_1("^v^v^v^v^v"))

    def test_transform_2(self):
        self.assertEqual(3, self.sut.solve_part_2("^v"))
        self.assertEqual(3, self.sut.solve_part_2("^>v<"))
        self.assertEqual(11, self.sut.solve_part_2("^v^v^v^v^v"))
