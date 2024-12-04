from itertools import product

from solver import Solver


class SolverImpl(Solver):

    _target_part_1 = "XMAS"
    _first_letter_part_1 = "X"

    _target_part_2 = "MAS"
    _first_letter_part_2 = "A"

    def solve_part_1(self, data: str) -> int:
        grid: list[str] = [
            line
            for line in data.strip().splitlines()
            if len(line) > 0
        ]
        rows = len(grid)
        cols = len(grid[0])
        total = 0
        for row, col in product(range(rows), range(cols)):
            if grid[row][col] != self._first_letter_part_1:
                continue
            fits_right = col < cols - 3
            fits_down = row < rows - 3
            fits_up = row > 2
            fits_left = col > 2
            # east
            if fits_right and (self._target_part_1 == grid[row][col:col + 4]):
                total += 1
            # south east
            if fits_right and fits_down and (self._target_part_1 == grid[row][col] + grid[row + 1][col + 1] + grid[row + 2][col + 2] + grid[row + 3][col + 3]):
                total += 1
            # south
            if fits_down and (self._target_part_1 == grid[row][col] + grid[row + 1][col] + grid[row + 2][col] + grid[row + 3][col]):
                total += 1
            # south west
            if fits_left and fits_down and (self._target_part_1 == grid[row][col] + grid[row + 1][col - 1] + grid[row + 2][col - 2] + grid[row + 3][col - 3]):
                total += 1
            # west
            if fits_left and (self._target_part_1 == grid[row][col - 3:col + 1][::-1]):
                total += 1
            # north west
            if fits_left and fits_up and (self._target_part_1 == grid[row][col] + grid[row - 1][col - 1] + grid[row - 2][col - 2] + grid[row - 3][col - 3]):
                total += 1
            # north
            if fits_up and (self._target_part_1 == grid[row][col] + grid[row - 1][col] + grid[row - 2][col] + grid[row - 3][col]):
                total += 1
            # north east
            if fits_right and fits_up and (self._target_part_1 == grid[row][col] + grid[row - 1][col + 1] + grid[row - 2][col + 2] + grid[row - 3][col + 3]):
                total += 1

        return total
    def solve_part_2(self, data: str) -> int:
        grid: list[str] = [
            line
            for line in data.strip().splitlines()
            if len(line) > 0
        ]
        rows = len(grid)
        cols = len(grid[0])
        total = 0
        for row, col in product(range(rows), range(cols)):
            if grid[row][col] != self._first_letter_part_2:
                continue
            fits = cols - 1 > col > 0 and rows - 1 > row > 0
            if not fits:
                continue
            a = grid[row + 1][col - 1] + grid[row][col] + grid[row - 1][col + 1]
            b = grid[row + 1][col + 1] + grid[row][col] + grid[row - 1][col - 1]
            if (a == self._target_part_2 or a[::-1] == self._target_part_2) \
                and (b == self._target_part_2 or b[::-1] == self._target_part_2):
                total += 1

        return total
