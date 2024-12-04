import sys
from pathlib import Path
from unittest import TestCase

import numpy
from solvers_2023.transformer_23 import SolverImpl

numpy.set_printoptions(threshold=sys.maxsize)


class TestTransformer23(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.sut = SolverImpl()

        file_path = Path(__file__)
        data_path = file_path.parents[2].joinpath("data", f"data_{file_path.name[-5:-3]}.txt")
        cls.real_data = data_path.read_text()
        cls.data = """#.#####################
#.......#########...###
#######.#########.#.###
###.....#.>.>.###.#.###
###v#####.#v#.###.#.###
###.>...#.#.#.....#...#
###v###.#.#.#########.#
###...#.#.#.......#...#
#####.#.#.#######.#.###
#.....#.#.#.......#...#
#.#####.#.#.#########v#
#.#...#...#...###...>.#
#.#.#v#######v###.###v#
#...#.>.#...>.>.#.###.#
#####v#.#.###v#.#.###.#
#.....#...#...#.#.#...#
#.#########.###.#.#.###
#...###...#...#...#.###
###.###.#.###v#####v###
#...#...#.#.>.>.#.>.###
#.###.###.#.###.#.#v###
#.....###...###...#...#
#####################.#"""

    def test_transform_1(self):
        self.assertEqual(94, self.sut.solve_part_1(self.data))

    def test_transform_1_real(self):
        self.assertEqual(2170, self.sut.solve_part_1(self.real_data))

    def test_transform_2(self):
        self.assertEqual(154, self.sut.solve_part_2(self.data))

    # def test_transform_2_real(self):
    #     self.assertLess(4946, self.sut.transform_2(self.real_data))
