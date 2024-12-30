from unittest import TestCase

from solvers_2024.solver_12 import SolverImpl


class TestTransformer12(TestCase):
    sut: SolverImpl
    data: str

    @classmethod
    def setUpClass(cls):
        cls.sut = SolverImpl()
        cls.data = """
        """

    def test_transform_1(self):
        # act assert
        self.assertEqual(140, self.sut.solve_part_1("""AAAA
BBCD
BBCC
EEEC
"""))
        self.assertEqual(772, self.sut.solve_part_1("""OOOOO
OXOXO
OOOOO
OXOXO
OOOOO
"""))
        self.assertEqual(1930, self.sut.solve_part_1("""RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE
"""))

    def test_transform_2(self):
        # act assert
        self.assertEqual(80, self.sut.solve_part_2("""AAAA
BBCD
BBCC
EEEC
"""))
        self.assertEqual(436, self.sut.solve_part_2("""OOOOO
OXOXO
OOOOO
OXOXO
OOOOO
"""))
        self.assertEqual(236, self.sut.solve_part_2("""EEEEE
EXXXX
EEEEE
EXXXX
EEEEE
"""))
        self.assertEqual(368, self.sut.solve_part_2("""AAAAAA
AAABBA
AAABBA
ABBAAA
ABBAAA
AAAAAA
"""))
        self.assertEqual(1206, self.sut.solve_part_2("""RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE
"""))
