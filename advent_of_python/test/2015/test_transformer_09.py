from unittest import TestCase

from solvers_2015.transformer_09 import TransformerImpl


class TestTransformer09(TestCase):
    sut: TransformerImpl
    @classmethod
    def setUpClass(cls):
        cls.sut = TransformerImpl()

    def test_transform_1(self):
        self.assertEqual(605, self.sut.transform_1("""London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141"""))

    def test_transform_2(self):
        self.assertEqual(982, self.sut.transform_2("""London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141"""))
