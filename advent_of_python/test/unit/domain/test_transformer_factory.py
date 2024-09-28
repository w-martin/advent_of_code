from unittest import TestCase

from domain.transformer_02 import TransformerImpl
from domain.transformer_03 import TransformerImpl as TransformerImpl03
from domain.transformer_factory import TransformerFactory


class TestTransformerFactory(TestCase):
    def test_should_instantiate_transformer(self):
        # arrange
        sut = TransformerFactory()
        # act
        result = sut.new("02")
        # assert
        self.assertIsInstance(result, TransformerImpl)

    def test_should_instantiate_transformer_03(self):
        # arrange
        sut = TransformerFactory()
        # act
        result = sut.new("03")
        # assert
        self.assertIsInstance(result, TransformerImpl03)
