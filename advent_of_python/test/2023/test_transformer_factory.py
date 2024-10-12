from unittest import TestCase

from solvers_2023.transformer_02 import SolverImpl
from solvers_2023.transformer_03 import SolverImpl as TransformerImpl03
from solvers_2023.transformer_factory import TransformerFactory


class TestTransformerFactory(TestCase):
    def test_should_instantiate_transformer(self):
        # arrange
        sut = TransformerFactory()
        # act
        result = sut.new("02")
        # assert
        self.assertIsInstance(result, SolverImpl)

    def test_should_instantiate_transformer_03(self):
        # arrange
        sut = TransformerFactory()
        # act
        result = sut.new("03")
        # assert
        self.assertIsInstance(result, TransformerImpl03)
