from unittest import TestCase

from solvers_2015.transformer_02 import TransformerImpl


class TestTransformer01(TestCase):
    sut: TransformerImpl
    @classmethod
    def setUpClass(cls):
        cls.sut = TransformerImpl()

    def test_transform_1(self):
        self.assertEqual(58, self.sut.transform_1("2x3x4"))
        self.assertEqual(43, self.sut.transform_1("1x1x10"))

    def test_transform_2(self):
        self.assertEqual(34, self.sut.transform_2("2x3x4"))
        self.assertEqual(34, self.sut.transform_2("4x2x3"))
        self.assertEqual(14, self.sut.transform_2("1x1x10"))
