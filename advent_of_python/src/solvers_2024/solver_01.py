from collections import Counter, defaultdict

from functional import seq

from solver import Solver


class SolverImpl(Solver):
    _MAX_SIZE = 1_000

    def solver_part_1(self, data: str) -> int:
        left, right = self._parse_input(data)
        left = sorted(left)
        right = sorted(right)
        return seq(left).zip(right).starmap(lambda a, b: abs(a - b)).sum()

    def _parse_input(self, data):
        left = [0] * self._MAX_SIZE
        right = left.copy()
        i = 0
        for line in data.strip().splitlines(keepends=False):
            parts = line.strip().split()
            if len(parts) == 2:
                left[i] = int(parts[0])
                right[i] = int(parts[1])
                i += 1
        return left, right

    def solve_part_2(self, data: str) -> int:
        left, right = self._parse_input(data)
        right_counter = defaultdict(lambda: 0)
        right_counter.update(Counter(right))
        return seq(left).map(lambda left_value: left_value * right_counter[left_value]).sum()
