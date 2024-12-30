from unittest import TestCase

from solvers_2024.solver_10 import SolverImpl


class TestTransformer01(TestCase):
    sut: SolverImpl
    data: str

    @classmethod
    def setUpClass(cls):
        cls.sut = SolverImpl()
        cls.data = """
        """

    def test_transform_1(self):
        # act assert
        self.assertEqual(1, self.sut.solve_part_1("""0123
1234
8765
9876"""))
        self.assertEqual(2, self.sut.solve_part_1("""...0...
...1...
...2...
6543456
7.....7
8.....8
9.....9"""))
        self.assertEqual(4, self.sut.solve_part_1("""..90..9
...1.98
...2..7
6543456
765.987
876....
987...."""))
        self.assertEqual(3, self.sut.solve_part_1("""10..9..
2...8..
3...7..
4567654
...8..3
...9..2
.....01"""))
        self.assertEqual(36, self.sut.solve_part_1("""89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""))

    def test_transform_2(self):
        # act assert
        self.assertEqual(3, self.sut.solve_part_2(""".....0.
..4321.
..5..2.
..6543.
..7..4.
..8765.
..9....
"""))
        self.assertEqual(13, self.sut.solve_part_2("""..90..9
...1.98
...2..7
6543456
765.987
876....
987....
"""))
        self.assertEqual(227, self.sut.solve_part_2("""012345
123456
234567
345678
4.6789
56789.
"""))
        self.assertEqual(81, self.sut.solve_part_2("""89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732
"""))
