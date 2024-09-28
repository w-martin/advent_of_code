import sys
from pathlib import Path
from unittest import TestCase, skip

import numpy
from domain.transformer_21 import TransformerImpl

numpy.set_printoptions(threshold=sys.maxsize)


class TestTransformer21(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.sut = TransformerImpl()

        file_path = Path(__file__)
        data_path = file_path.parents[2].joinpath("data", f"data_{file_path.name[-5:-3]}.txt")
        cls.real_data = data_path.read_text()
        cls.data = """...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
..........."""

    def test_transform_1_1(self):
        self.assertEqual(16, self.sut.transform_1(self.data, 6))

    @skip("slow")
    def test_transform_2(self):
        self.assertEqual(16, self.sut.transform_2(self.data, 6))
        self.assertEqual(50, self.sut.transform_2(self.data, 10))
        self.assertEqual(1594, self.sut.transform_2(self.data, 50))

        for i in range(262):
            with open(f"test_transformer_21.csv", "a") as f:
                text = f"{i},{self.sut.transform_2(self.data, i)}\n"
                f.write(text)

        # self.assertEqual(6536, self.sut.transform_2(self.data, 100))
        # self.assertEqual(167004, self.sut.transform_2(self.data, 500))
        # self.assertEqual(668697, self.sut.transform_2(self.data, 1000))
        # self.assertEqual(16733044, self.sut.transform_2(self.data, 5000))
