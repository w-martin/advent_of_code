import sys
from pathlib import Path
from unittest import TestCase

import numpy
from solvers_2023.transformer_24 import TransformerImpl

numpy.set_printoptions(threshold=sys.maxsize)


class TestTransformer24(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.sut = TransformerImpl()

        file_path = Path(__file__)
        data_path = file_path.parents[2].joinpath("data", f"data_{file_path.name[-5:-3]}.txt")
        cls.real_data = data_path.read_text()
        cls.data = """19, 13, 30 @ -2,  1, -2
18, 19, 22 @ -1, -1, -2
20, 25, 34 @ -2, -2, -4
12, 31, 28 @ -1, -2, -1
20, 19, 15 @  1, -5, -3"""

    def test_transform_1(self):
        self.assertEqual(2, self.sut.transform_1(self.data, 7, 27))

    def test_path_xy_intersection(self):
        self.assertEqual((14.333, 15.333), self.sut._get_intersection_point((19, 13), (-2, 1), (18, 19), (-1, -1)))
        self.assertEqual((11.667, 16.667), self.sut._get_intersection_point((19, 13), (-2, 1), (20, 25), (-2, -2)))
        self.assertEqual((6.2, 19.4), self.sut._get_intersection_point((19, 13), (-2, 1), (12, 31), (-1, -2)))

    def test_transform_1_real(self):
        result = self.sut.transform_1(self.real_data, 200000000000000, 400000000000000)
        self.assertLess(5181, result)
        self.assertEqual(20847, result)

    def test_transform_2(self):
        self.assertEqual(47, self.sut.transform_2(self.data))

    # def test_transform_2_real(self):
    #     self.assertLess(4946, self.sut.transform_2(self.real_data))
