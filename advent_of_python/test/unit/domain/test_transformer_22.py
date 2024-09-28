import sys
from pathlib import Path
from unittest import TestCase

import numpy
from domain.transformer_22 import TransformerImpl

numpy.set_printoptions(threshold=sys.maxsize)


class TestTransformer22(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.sut = TransformerImpl()

        file_path = Path(__file__)
        data_path = file_path.parents[2].joinpath("data", f"data_{file_path.name[-5:-3]}.txt")
        cls.real_data = data_path.read_text()
        cls.data = """1,0,1~1,2,1
0,0,2~2,0,2
0,2,3~2,2,3
0,0,4~0,2,4
2,0,5~2,2,5
0,1,6~2,1,6
1,1,8~1,1,9
"""

    def test_transform_1(self):
        self.assertEqual(5, self.sut.transform_1(self.data))

    def test_transform_1_real(self):
        actual = self.sut.transform_1(self.real_data)
        self.assertNotEqual(410, actual)
        self.assertNotEqual(669, actual)
        self.assertNotEqual(670, actual)
        self.assertNotEqual(218, actual)
        self.assertEqual(409, actual)

    def test_transform_2(self):
        self.assertEqual(7, self.sut.transform_2(self.data))
