from pathlib import Path
from unittest import TestCase

from solvers_2015.transformer_01 import TransformerImpl


class TestTransformer01(TestCase):
    sut: TransformerImpl
    @classmethod
    def setUpClass(cls):
        cls.sut = TransformerImpl()

    def test_transform_1(self):
        self.assertEqual(0, self.sut.transform_1("(())"))
        self.assertEqual(0, self.sut.transform_1("()()"))
        self.assertEqual(3, self.sut.transform_1("((("))
        self.assertEqual(3, self.sut.transform_1("(()(()("))
        self.assertEqual(3, self.sut.transform_1("))((((("))
        self.assertEqual(-1, self.sut.transform_1("())"))
        self.assertEqual(-1, self.sut.transform_1("))("))
        self.assertEqual(-3, self.sut.transform_1(")))"))
        self.assertEqual(-3, self.sut.transform_1(")())())"))

    def test_transform_2(self):
        self.assertEqual(1, self.sut.transform_2(")"))
        self.assertEqual(5, self.sut.transform_2("()())"))
