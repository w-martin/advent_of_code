from enum import Enum
from itertools import product

import numpy as np
from functional import seq

from solver import Solver


class Direction(Enum):
    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)


class SolverImpl(Solver):

    def __init__(self):
        self._height: int | None = None
        self._width: int | None = None
        self._visited: np.ndarray | None = None
        self._obstacles: np.ndarray | None = None
        self._position: tuple[int, int] | None = None
        self._direction: Direction | None = None
        self._position_directions: set[tuple[int, int, Direction]] = set()
        self._off_grid = False
        self._looping = False

    directions = {
        '^': Direction.UP, 'v': Direction.DOWN, '<': Direction.LEFT, '>': Direction.RIGHT
    }

    def solve_part_1(self, data: str) -> int:
        self._initialise(data)
        while self._move():
            ...
        return self._visited.sum()

    def _initialise(self, data):
        lines = data.strip().splitlines(keepends=False)
        self._height = len(lines)
        self._width = len(lines[0])
        self._visited = np.zeros((self._height, self._width), dtype=bool)
        self._obstacles = np.array(
            seq(lines).map(list).map(lambda l: seq(l).map(lambda li: "#" == li).to_list()).to_list()).T
        for j, i in product(range(self._height), range(self._width)):
            char = lines[j][i]
            if char in ('<', '>', '^', 'v'):
                self._position = (i, j)
                self._direction = self.directions[char]
                self._visited[i, j] = True
                break
        assert self._position, "Position not found"

    def solve_part_2(self, data: str) -> int:
        self._initialise(data)
        starting_position = self._position
        starting_direction = self._direction
        while self._move():
            ...
        potential_obstacle_positions = set(zip(np.where(self._visited)[0].tolist(), np.where(self._visited)[1].tolist())) - {starting_position, }
        original_obstacles = self._obstacles
        total = 0
        for obstacle_position in potential_obstacle_positions:
            self._position = starting_position
            self._direction = starting_direction
            self._visited[:, :] = False
            self._visited[self._position[0], self._position[1]] = True
            self._obstacles = original_obstacles.copy()
            self._obstacles[obstacle_position[0], obstacle_position[1]] = True
            self._off_grid = False
            self._looping = False
            self._position_directions = {(self._position[0], self._position[1], self._direction)}
            while self._move():
                ...
            if self._looping:
                total += 1

        return total

    def _in_grid(self, position):
        return 0 <= position[0] < self._width and 0 <= position[1] < self._height

    def _move(self) -> bool:
        new_position = (self._position[0] + self._direction.value[0], self._position[1] + self._direction.value[1])
        if not self._in_grid(new_position):
            self._off_grid = True
            return False
        if self._obstacles[new_position[0], new_position[1]]:
            self._turn_right()
            return self._move()
        else:
            self._position = new_position
            self._visited[new_position[0], new_position[1]] = True
            new_position_direction = (*new_position, self._direction)
            if new_position_direction in self._position_directions:
                self._looping = True
                return False
            else:
                self._position_directions.add(new_position_direction)
                return True

    def _turn_right(self):
        match self._direction:
            case Direction.UP:
                self._direction = Direction.RIGHT
            case Direction.RIGHT:
                self._direction = Direction.DOWN
            case Direction.DOWN:
                self._direction = Direction.LEFT
            case Direction.LEFT:
                self._direction = Direction.UP

    def _print(self):
        print()
        for j in range(self._height):
            for i in range(self._width):
                if self._position == (i, j):
                    print(self._direction.name[0], end="")
                elif self._visited[i, j]:
                    print("X", end="")
                elif self._obstacles[i, j]:
                    print("#", end="")
                else:
                    print(".", end="")
            print()
        print()
