from pathlib import Path
from unittest import TestCase

from domain.transformer_01 import TransformerImpl


class TestTransformer01(TestCase):
    sut: TransformerImpl
    @classmethod
    def setUpClass(cls):
        cls.real_data = (Path(__file__).parents[4] / "data" / "2023" / "day_01.txt").read_text("utf-8")
        cls.sut = TransformerImpl()

    def test_transform_1(self):
        # arrange
        data = (Path(__file__).parents[4] / "data" / "2023" / "day_01_example_part_1.txt").read_text("utf-8")
        # act assert
        self.assertEqual(142, self.sut.transform_1(data))

    def test_transform_2(self):
        # arrange
        data = (Path(__file__).parents[4] / "data" / "2023" / "day_01_example_part_2.txt").read_text("utf-8")
        # act assert
        self.assertEqual(281, self.sut.transform_2(data))

    def test_transform_1_real_data(self):
        # act assert
        self.assertEqual(55386, self.sut.transform_1(self.real_data))

    def test_transform_2_real_data(self):
        # act assert
        self.assertEqual(54824, self.sut.transform_2(self.real_data))
