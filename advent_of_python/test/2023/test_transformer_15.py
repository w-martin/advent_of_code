import sys
from pathlib import Path
from unittest import TestCase

import numpy

from solvers_2023.transformer_15 import SolverImpl

numpy.set_printoptions(threshold=sys.maxsize)


class TestTransformer15(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.sut = SolverImpl()

        file_path = Path(__file__)
        data_path = file_path.parents[2].joinpath("data", f"data_{file_path.name[-5:-3]}.txt")
        cls.real_data = data_path.read_text()

    def test_transform_1(self):
        self.assertEqual(1320, self.sut.solver_part_1("""rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"""))

    def test_transform_2(self):
        self.assertEqual(145, self.sut.solve_part_2("""rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"""))
