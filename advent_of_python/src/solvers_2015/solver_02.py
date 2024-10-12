import math
from typing import Any

from functional import seq

from solver import Solver


class SolverImpl(Solver):

    def solver_part_1(self, data: str) -> Any:
        return (
            seq(data.splitlines(keepends=False))
            .map(self._transform_line_1)
            .sum()
        )

    def _transform_line_1(self, data):
        l, w, h = tuple(map(int, data.strip().split("x")))
        sides = (
            l * w,
            w * h,
            h * l,
        )
        return 2 * sum(sides) + min(sides)

    def solve_part_2(self, data: str) -> Any:
        return (
            seq(data.splitlines(keepends=False))
            .map(self._transform_line_2)
            .sum()
        )

    def _transform_line_2(self, data: str) -> int:
        edges = list(map(int, data.strip().split("x")))
        return 2 * sum(sorted(edges)[:2]) + math.prod(edges)
