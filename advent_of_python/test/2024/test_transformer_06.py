from unittest import TestCase

from solvers_2024.solver_06 import SolverImpl


class TestTransformer01(TestCase):
    sut: SolverImpl
    data: str

    @classmethod
    def setUpClass(cls):
        cls.sut = SolverImpl()
        cls.data = """
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
        """

    def test_transform_1(self):
        # act assert
        self.assertEqual(41, self.sut.solve_part_1(self.data))

    def test_transform_2(self):
        # act assert
        self.assertEqual(6, self.sut.solve_part_2(self.data))
