from unittest import TestCase

from solvers_2024.solver_05 import SolverImpl


class TestTransformer01(TestCase):
    sut: SolverImpl
    data: str

    @classmethod
    def setUpClass(cls):
        cls.sut = SolverImpl()
        cls.data = """
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47

        """

    def test_transform_1(self):
        # act assert
        self.assertEqual(143, self.sut.solve_part_1(self.data))

    def test_transform_2(self):
        # act assert
        self.assertEqual(123, self.sut.solve_part_2(self.data))

    def test_should_sort_parts(self):
        # arrange
        parts = [2, 4, 3, 1]
        rules = {
            2: {1},
            3: {1, 2},
            4: {1, 2, 3}
        }
        expected = [1, 2, 3, 4]
        # act
        actual = self.sut.sort_by_rules(parts, rules)
