import re
from enum import Enum, auto
from typing import Any

from solver import Solver
from solver_error import SolverError


class SolverImpl(Solver):
    regex = re.compile(r"([LR])(\d+)")

    class Direction(Enum):
        north = auto()
        south = auto()
        east = auto()
        west = auto()

    def _solve(self, data: str, break_on_visited: bool) -> tuple[int, int]:
        visited = set()
        direction = self.Direction.north
        position = (0, 0)
        if break_on_visited:
            visited.add(position)
        for match in self.regex.finditer(data):
            direction = self._apply_direction(match.group(1), direction)
            distance = int(match.group(2))
            while distance > 0:
                position = self._move(position, direction)
                if break_on_visited:
                    if position in visited:
                        return position
                    else:
                        visited.add(position)
                distance -= 1
        return position

    def solve_part_1(self, data: str) -> Any:
        solution = self._solve(data, False)
        return self._get_distance(solution)

    def _apply_direction(self, c: str, direction: Direction) -> Direction:
        if "L" == c:
            direction = self._turn_left(direction)
        elif "R" == c:
            direction = self._turn_right(direction)
        return direction

    def solve_part_2(self, data: str) -> Any:
        solution = self._solve(data, True)
        return self._get_distance(solution)

    def _turn_left(self, direction: Direction) -> Direction:
        match direction:
            case self.Direction.north:
                return self.Direction.west
            case self.Direction.west:
                return self.Direction.south
            case self.Direction.south:
                return self.Direction.east
            case self.Direction.east:
                return self.Direction.north
        raise SolverError("Couldn't turn left")

    def _turn_right(self, direction: Direction) -> Direction:
        match direction:
            case self.Direction.north:
                return self.Direction.east
            case self.Direction.east:
                return self.Direction.south
            case self.Direction.south:
                return self.Direction.west
            case self.Direction.west:
                return self.Direction.north
        raise SolverError("Couldn't turn right")

    def _move(self, position: tuple[int, int], direction: Direction) -> tuple[int, int]:
        match direction:
            case self.Direction.north:
                return position[0], position[1] + 1
            case self.Direction.south:
                return position[0], position[1] - 1
            case self.Direction.east:
                return position[0] + 1, position[1]
            case self.Direction.west:
                return position[0] - 1, position[1]
        raise SolverError("Couldn't move")

    def _get_distance(self, solution: tuple[int, int]) -> int:
        return abs(solution[0]) + abs(solution[1])
