import sys
from pathlib import Path
from unittest import TestCase

import numpy

from solvers_2023.transformer_14 import SolverImpl

numpy.set_printoptions(threshold=sys.maxsize)


class TestTransformer11(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.sut = SolverImpl()

        file_path = Path(__file__)
        data_path = file_path.parents[2].joinpath("data", f"data_{file_path.name[-5:-3]}.txt")
        cls.real_data = data_path.read_text()

    def test_transform_1(self):
        self.assertEqual(136, self.sut.solver_part_1("""O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#...."""))

    def test_transform_2(self):
        self.assertEqual(64, self.sut.solve_part_2("""O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#...."""))
