import sys
from pathlib import Path
from unittest import TestCase

import numpy
from domain.transformer_25 import TransformerImpl

numpy.set_printoptions(threshold=sys.maxsize)


class TestTransformer25(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.sut = TransformerImpl()

        file_path = Path(__file__)
        data_path = file_path.parents[2].joinpath("data", f"data_{file_path.name[-5:-3]}.txt")
        cls.real_data = data_path.read_text()
        cls.data = """jqt: rhn xhk nvd
rsh: frs pzl lsr
xhk: hfx
cmg: qnr nvd lhk bvb
rhn: xhk bvb hfx
bvb: xhk hfx
pzl: lsr hfx nvd
qnr: nvd
ntq: jqt hfx bvb xhk
nvd: lhk
lsr: lhk
rzs: qnr cmg lsr rsh
frs: qnr lhk lsr
"""

    def test_transform_1(self):
        self.assertEqual(54, self.sut.transform_1(self.data))

    # def test_transform_1_real(self):
    #     result = self.sut.transform_1(self.real_data, 200000000000000, 400000000000000)
    #     self.assertLess(5181, result)
    #     self.assertEqual(20847, result)

    # def test_transform_2(self):
    #     self.assertEqual(47, self.sut.transform_2(self.data))

    # def test_transform_2_real(self):
    #     self.assertLess(4946, self.sut.transform_2(self.real_data))
