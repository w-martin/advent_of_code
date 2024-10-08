import sys
from pathlib import Path
from unittest import TestCase

import numpy

from solvers_2023.transformer_11 import TransformerImpl

numpy.set_printoptions(threshold=sys.maxsize)


class TestTransformer11(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.sut = TransformerImpl()

        file_path = Path(__file__)
        data_path = file_path.parents[2].joinpath("data", f"data_{file_path.name[-5:-3]}.txt")
        cls.real_data = data_path.read_text()

    def test_transform_1(self):
        self.assertEqual(374, self.sut.transform_1("""...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#....."""))

    def test_transform_2(self):
        self.assertEqual(1030, self.sut.with_expansion_factor(10).transform_1("""...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#....."""))
        self.assertEqual(8410, self.sut.with_expansion_factor(100).transform_1("""...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#....."""))