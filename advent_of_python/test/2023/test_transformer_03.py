import sys
from pathlib import Path
from unittest import TestCase

import numpy

from solvers_2023.transformer_03 import SolverImpl

numpy.set_printoptions(threshold=sys.maxsize)


class TestTransformer03(TestCase):

    def test_transform_1(self):
        data = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""
        sut = SolverImpl()
        self.assertEqual(4361, sut.solve_part_1(data))

    def test_transformer_1_with_real(self):
        file_path = Path(__file__)
        data_path = file_path.parents[2].joinpath("data", f"data_{file_path.name[-5:-3]}.txt")
        data = data_path.read_text()
        sut = SolverImpl()
        result = sut.solve_part_1(data)
        self.assertLess(result, 528686)
        self.assertGreater(result, 327640)
        self.assertNotEqual(521740, result)

    def test_transform_2(self):
        data = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""
        sut = SolverImpl()
        self.assertEqual(467835, sut.solve_part_2(data))
