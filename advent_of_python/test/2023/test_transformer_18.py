import sys
from pathlib import Path
from unittest import TestCase

import numpy
from solvers_2023.transformer_18 import SolverImpl

numpy.set_printoptions(threshold=sys.maxsize)


class TestTransformer18(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.sut = SolverImpl()

        file_path = Path(__file__)
        data_path = file_path.parents[2].joinpath("data", f"data_{file_path.name[-5:-3]}.txt")
        cls.real_data = data_path.read_text()
        cls.data = """R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)"""

    def test_transform_1(self):
        self.assertEqual(62, self.sut.solver_part_1(self.data))

    def test_transform_1_real(self):
        self.assertGreater(46340, self.sut.solver_part_1(self.real_data))

    def test_transform_2(self):
        self.assertEqual(952408144115, self.sut.solve_part_2(self.data))
