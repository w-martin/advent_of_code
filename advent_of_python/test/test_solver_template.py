from unittest import TestCase

from solver_template import SolverImpl


class TestTransformerTemplate(TestCase):
    sut: SolverImpl
    @classmethod
    def setUpClass(cls):
        cls.sut = SolverImpl()

    def test_transform_1(self):
        self.assertEqual(0, self.sut.solve_part_1(""))

    def test_transform_2(self):
        self.assertEqual(0, self.sut.solve_part_2(""))
