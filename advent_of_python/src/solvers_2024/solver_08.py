from itertools import combinations

import numpy as np

from solver import Solver


class SolverImpl(Solver):

    def solve_part_1(self, data: str) -> int:
        data = data.strip()
        unique_nodes = set(data) - {'\n', '.'}
        data_array = np.vstack([np.array(list(line)) for line in data.splitlines(keepends=False)])
        antinodes = np.zeros_like(data_array, dtype=bool)
        for node in unique_nodes:
            locations = list(zip(*(item.tolist() for item in np.where(data_array == node))))
            for (y1, x1), (y2, x2) in combinations(locations, 2):
                vector = y2 - y1, x2 - x1
                for x, y in (
                        (y1 - vector[0], x1 - vector[1]),
                        (y2 + vector[0], x2 + vector[1]),
                ):
                    if 0 <= x < data_array.shape[0] and 0 <= y < data_array.shape[1]:
                        antinodes[x, y] = True
        # self._print(data_array, antinodes)
        return int(antinodes.sum())

    def solve_part_2(self, data: str) -> int:
        data = data.strip()
        unique_nodes = set(data) - {'\n', '.'}
        data_array = np.vstack([np.array(list(line)) for line in data.splitlines(keepends=False)])
        antinodes = np.zeros_like(data_array, dtype=bool)
        for node in unique_nodes:
            locations = list(zip(*(item.tolist() for item in np.where(data_array == node))))
            for (y1, x1), (y2, x2) in combinations(locations, 2):
                vector = y2 - y1, x2 - x1
                x, y = y1, x1
                while 0 <= x < data_array.shape[0] and 0 <= y < data_array.shape[1]:
                    antinodes[x, y] = True
                    x, y = x - vector[0], y - vector[1]
                x, y = y2, x2
                while 0 <= x < data_array.shape[0] and 0 <= y < data_array.shape[1]:
                    antinodes[x, y] = True
                    x, y = x + vector[0], y + vector[1]
        return int(antinodes.sum())

    def _print(self, data_array, antinodes):
        for x in range(data_array.shape[0]):
            for y in range(data_array.shape[1]):
                if antinodes[x, y]:
                    print('#', end='')
                else:
                    print(data_array[x, y], end='')
            print()
