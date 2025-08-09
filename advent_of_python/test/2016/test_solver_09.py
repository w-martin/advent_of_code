from unittest import TestCase

from solvers_2016.solver_09 import SolverImpl


class TestSolver09(TestCase):
    sut: SolverImpl
    @classmethod
    def setUpClass(cls):
        cls.sut = SolverImpl()

    def test_transform_1(self):
        self.assertEqual(6, self.sut.solve_part_1("ADVENT"))
        self.assertEqual(7, self.sut.solve_part_1("A(1x5)BC"))
        self.assertEqual(9, self.sut.solve_part_1("(3x3)XYZ"))
        self.assertEqual(11, self.sut.solve_part_1("A(2x2)BCD(2x2)EFG"))
        self.assertEqual(6, self.sut.solve_part_1("(6x1)(1x3)A"))
        self.assertEqual(18, self.sut.solve_part_1("X(8x2)(3x3)ABCY"))

    def test_transform_2(self):
        self.assertEqual(len("XYZXYZXYZ"), self.sut.solve_part_2("(3x3)XYZ"))
        self.assertEqual(len("XABCABCABCABCABCABCY"), self.sut.solve_part_2("X(8x2)(3x3)ABCY"))
        self.assertEqual(241920, self.sut.solve_part_2("(27x12)(20x12)(13x14)(7x10)(1x12)A"))
        self.assertEqual(445, self.sut.solve_part_2("(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN"))
