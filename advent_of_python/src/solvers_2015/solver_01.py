from typing import Any

from solver import Solver


class SolverImpl(Solver):

    def solve_part_1(self, data: str) -> Any:
        result_floor = 0
        for character in data:
            match character:
                case '(':
                    result_floor += 1
                case ')':
                    result_floor -= 1
        return result_floor

    def solve_part_2(self, data: str) -> Any:
        result_floor = 0
        for i, character in enumerate(data):
            match character:
                case '(':
                    result_floor += 1
                case ')':
                    result_floor -= 1
            if result_floor < 0:
                return 1 + i
        return -1
