from collections import Counter, defaultdict

from functional import seq

from solver import Solver


class SolverImpl(Solver):
    def __init__(self):
        self._stones_that_split = {}

    def solve_part_1(self, data: str) -> int:
        return self.blink(data, 25)

    def solve_part_2(self, data: str) -> int:
        return self.blink(data, 75)

    def blink(self, data: str, num_blinks: int):
        stones = Counter(seq(data.strip().split()).map(int))
        for i in range(num_blinks):
            stones = self._blink(stones)
        return sum(stones.values())

    def _blink(self, stones: dict[int, int]):
        new_stones = defaultdict(int)
        for stone, count in stones.items():
            if stone == 0:
                new_stones[1] += count
            elif stone in self._stones_that_split:
                left_stone, right_stone = self._stones_that_split[stone]
                new_stones[left_stone] += count
                new_stones[right_stone] += count
            else:
                if len((stone_str := str(stone))) % 2 == 0:
                    half_len = len(stone_str) // 2
                    left_stone = int(stone_str[:half_len])
                    new_stones[left_stone] += count
                    right_stone = int(stone_str[half_len:])
                    new_stones[right_stone] += count
                    self._stones_that_split[stone] = (left_stone, right_stone)
                else:
                    new_stones[stone * 2024] += count
        return new_stones
