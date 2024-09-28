import sys
from pathlib import Path
from unittest import TestCase

import numpy
from domain.transformer_20 import TransformerImpl

numpy.set_printoptions(threshold=sys.maxsize)


class TestTransformer20(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.sut = TransformerImpl()

        file_path = Path(__file__)
        data_path = file_path.parents[2].joinpath("data", f"data_{file_path.name[-5:-3]}.txt")
        cls.real_data = data_path.read_text()

    def test_transform_1_1(self):
        self.assertEqual(32000000, self.sut.transform_1("""broadcaster -> a, b, c
%a -> b
%b -> c
%c -> inv
&inv -> a"""))

    def test_transform_1_2(self):
        self.assertEqual(11687500, self.sut.transform_1("""broadcaster -> a
%a -> inv, con
&inv -> b
%b -> con
&con -> output"""))

    def test_transform_2(self):
        return
        self.assertEqual(167409079868000, self.sut.transform_2(self.data))
