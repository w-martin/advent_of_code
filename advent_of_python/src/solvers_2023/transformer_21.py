import numpy as np

from functools import lru_cache
from pathlib import Path
from typing import Any

from solver import Solver


class SolverImpl(Solver):

    def __init__(self):
        self._arr = None

    def solve_part_1(self, data: str, num_steps: int) -> Any:

        lines = []
        for line in data.splitlines(False):
            line = line.strip()
            if len(line) > 0:
                lines.append(line)

        arr = np.array([list(line) for line in lines])
        start = np.where(arr == 'S')
        arr = self._arr = arr == '#'

        visited = self._visit_1((start[0][0], start[1][0]), num_steps)

        return len(visited)

    @lru_cache(maxsize=None)
    def _visit_1(self, start: tuple[int, int], num_steps: int) -> set[tuple[int, int]]:
        if num_steps == 0:
            return {start}
        else:
            visited = set()
            for neighbour in self._get_neighbours_1(start):
                visited.update(self._visit_1(neighbour, num_steps - 1))
            return visited

    @lru_cache(maxsize=None)
    def _visit_2(self, start: tuple[int, int], num_steps: int) -> set[tuple[int, int]]:
        if num_steps == 0:
            return {start}
        else:
            visited = set()
            for neighbour in self._get_neighbours_2(start):
                visited.update(self._visit_2(neighbour, num_steps - 1))
            return visited

    @lru_cache(maxsize=None)
    def _get_neighbours_1(self, position: tuple[int, int]) -> list[tuple[int, int]]:
        result = []
        for direction in (
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0),
        ):
            new_position = (position[0] + direction[0], position[1] + direction[1])
            if 0 <= new_position[0] < self._arr.shape[0] and 0 <= new_position[1] < self._arr.shape[1] and not self._arr[new_position]:
                result.append(new_position)
        return result

    @lru_cache(maxsize=None)
    def _get_neighbours_2(self, position: tuple[int, int]) -> list[tuple[int, int]]:
        result = []
        for direction in (
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0),
        ):
            new_position = (position[0] + direction[0], position[1] + direction[1])
            if not self._arr[new_position[0] % self._arr.shape[0]][new_position[1] % self._arr.shape[1]]:
                result.append(new_position)
        return result

    def solve_part_2(self, data: str, num_steps: int) -> Any:
        lines = []
        for line in data.splitlines(False):
            line = line.strip()
            if len(line) > 0:
                lines.append(line)

        arr = np.array([list(line) for line in lines])
        start = np.where(arr == 'S')
        self._arr = arr == '#'

        visited = self._visit_2((start[0][0], start[1][0]), num_steps)

        return len(visited)


if __name__ == "__main__":
    file_path = Path(__file__)
    data_path = file_path.parents[2].joinpath("data", f"data_{file_path.name[-5:-3]}.txt")
    data = data_path.read_text()
    sut = SolverImpl()
    print(sut.solve_part_1(data, 64))
    answer_2 = sut.solve_part_2(data, 26501365)
    print(answer_2)
