from unittest import TestCase

from solvers_2016.solver_08 import SolverImpl


class TestSolver08(TestCase):
    sut: SolverImpl
    @classmethod
    def setUpClass(cls):
        cls.sut = SolverImpl()

    def test_transform_1(self):
        self.assertEqual(6, self.sut.solve_part_1("""
        rect 3x2
        rotate column x=1 by 1
        rotate row y=0 by 4
        rotate column x=1 by 1"""))

    def test_transform_2(self):
        ...
