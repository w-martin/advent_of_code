import sys
from pathlib import Path
from unittest import TestCase

import numpy

from solvers_2023.transformer_09 import SolverImpl

numpy.set_printoptions(threshold=sys.maxsize)


class TestTransformer09(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.data = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""
        cls.sut = SolverImpl()

        file_path = Path(__file__)
        data_path = file_path.parents[2].joinpath("data", f"data_{file_path.name[-5:-3]}.txt")
        cls.real_data = data_path.read_text()

    def test_transform_1(self):
        self.assertEqual(114, self.sut.solve_part_1(self.data))

    def test_transform_1_real(self):
        result = self.sut.solve_part_1(self.real_data)
        self.assertGreater(1748059900, result)
        self.assertGreater(1745741424, result)

    def test_transform_2(self):
        self.assertEqual(2, self.sut.solve_part_2(self.data))
