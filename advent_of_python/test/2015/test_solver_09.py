from unittest import TestCase

from solvers_2015.solver_09 import SolverImpl


class TestTransformer09(TestCase):
    sut: SolverImpl
    @classmethod
    def setUpClass(cls):
        cls.sut = SolverImpl()
        cls.data = """London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141"""

    def test_transform_1(self):
        self.assertEqual(605, self.sut.solver_part_1(self.data))

    def test_transform_2(self):
        self.assertEqual(982, self.sut.solve_part_2(self.data))
