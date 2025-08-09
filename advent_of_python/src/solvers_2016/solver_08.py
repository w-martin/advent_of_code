import numpy as np
from solver import Solver


class SolverImpl(Solver):
    def solve_part_1(self, data: str) -> int:
        grid = np.zeros(shape=(6, 50), dtype=bool)
        for line in data.strip().splitlines():
            line = line.strip()
            if line.startswith("rect"):
                x, y = map(int, line[5:].split("x"))
                grid[:y, :x] = True
            elif line.startswith("rotate column"):
                x = int(line.split("=")[1].split()[0])
                shift = int(line.split()[-1])
                grid[:, x] = np.roll(grid[:, x], shift)
            elif line.startswith("rotate row"):
                y = int(line.split("=")[1].split()[0])
                shift = int(line.split()[-1])
                grid[y, :] = np.roll(grid[y, :], shift)
        self._print(grid)
        return grid.astype(int).sum()

    def solve_part_2(self, data: str) -> int:
        pass

    def _print(self, grid):
        for row in grid:
            print("".join("#" if cell else "." for cell in row))
        print()
