from unittest import TestCase

from solvers_2015.solver_01 import SolverImpl


class TestTransformer01(TestCase):
    sut: SolverImpl
    @classmethod
    def setUpClass(cls):
        cls.sut = SolverImpl()

    def test_transform_1(self):
        self.assertEqual(0, self.sut.solver_part_1("(())"))
        self.assertEqual(0, self.sut.solver_part_1("()()"))
        self.assertEqual(3, self.sut.solver_part_1("((("))
        self.assertEqual(3, self.sut.solver_part_1("(()(()("))
        self.assertEqual(3, self.sut.solver_part_1("))((((("))
        self.assertEqual(-1, self.sut.solver_part_1("())"))
        self.assertEqual(-1, self.sut.solver_part_1("))("))
        self.assertEqual(-3, self.sut.solver_part_1(")))"))
        self.assertEqual(-3, self.sut.solver_part_1(")())())"))

    def test_transform_2(self):
        self.assertEqual(1, self.sut.solve_part_2(")"))
        self.assertEqual(5, self.sut.solve_part_2("()())"))
