import itertools
import re
from collections import deque
from copy import copy
from dataclasses import dataclass, field
from functools import partial
from pathlib import Path
from typing import Any

import numpy as np
from functional import seq

from solver import Solver


@dataclass
class Shape:
    id: int
    x1: int
    y1: int
    z1: int
    x2: int
    y2: int
    z2: int
    supported_by: set[int] = field(default_factory=set)
    falling: bool = True

    def equals(self, other: 'Shape') -> bool:
        return (
                self.x1 == other.x1
                and self.y1 == other.y1
                and self.z1 == other.z1
                and self.x2 == other.x2
                and self.y2 == other.y2
                and self.z2 == other.z2
        )


class SolverImpl(Solver):

    def solver_part_1(self, data: str) -> Any:
        shapes = self._parse_shapes(data)
        supports, supported_by = self._fall(shapes)
        shapes_that_cannot_be_dissolved = seq(supported_by.values()).filter(lambda x: len(x) == 1).flatten().to_set()
        result = len(shapes) - len(
            shapes_that_cannot_be_dissolved
        )
        return result

    def _parse_shapes(self, data):
        shapes = []
        id: int = 1
        for line in data.splitlines(False):
            line = line.strip()
            if len(line) > 0:
                # 0,0,2~2,0,2
                match = re.match(r"(\d+),(\d+),(\d+)~(\d+),(\d+),(\d+)", line)
                shape = Shape(id, *map(int, match.groups()))
                shapes.append(shape)
                id += 1
        return shapes

    def _fall_without_equals(self, shapes: list[Shape], all_fallen: list[Shape], shape: Shape):
        shapes_without_shape = seq(shapes).filter(lambda x: x.id != shape.id).map(copy).to_list()
        fallen = self._fall(shapes_without_shape)
        expected = seq(all_fallen).filter(lambda x: x.id != shape.id).to_list()
        result = fallen == expected
        return result

    def _fall(self, shapes: list[Shape]) -> dict[int, set[int]]:
        max_x = seq(shapes).map(lambda shape: shape.x2).max() + 1
        max_y = seq(shapes).map(lambda shape: shape.y2).max() + 1
        max_z = seq(shapes).map(lambda shape: shape.z2).max() + 1
        grid = np.zeros((max_x, max_y, max_z), dtype=int)
        supports: dict[int, set[int]] = {
            shape.id: set()
            for shape in shapes
        }
        supported_by: dict[int, set[int]] = {
            shape.id: set()
            for shape in shapes
        }
        # init grid
        for shape in seq(shapes).sorted(key=lambda shape: shape.z1):
            shape_points = itertools.product(range(shape.x1, shape.x2 + 1), range(shape.y1, shape.y2 + 1),
                                             range(shape.z1, shape.z2 + 1))

            for x, y, z in shape_points:
                grid[x, y, z] = shape.id
        falling_mask = grid > 0
        fallen_mask = np.zeros_like(grid, dtype=bool)
        fallen_mask[:, :, 0] = True
        while falling_mask.any():
            rolled = np.roll(np.where(falling_mask, grid, 0), -1, axis=2)
            collision = ((rolled > 0) & fallen_mask).astype(bool)
            ...
            if collision.any():
                objects_that_cant_fall = np.unique(grid[np.roll(collision, 1, 2)])
                ...
                for object_that_cant_fall in objects_that_cant_fall:
                    object_mask = grid == object_that_cant_fall
                    fallen_mask += object_mask
                    falling_mask ^= object_mask
            else:
                grid = np.where(~fallen_mask, rolled, grid)
                falling_mask = np.roll(falling_mask, -1, axis=2)
        for shape in shapes:
            object_mask = grid == shape.id
            underneath_mask = np.roll(object_mask, -1, axis=2)
            supported_by_set = set(np.unique(grid[underneath_mask])) - {0, shape.id}
            # print(f"object {shape.id} is supported by {supported_by}")
            for supported_by_id in supported_by_set:
                supports[supported_by_id].add(shape.id)
                supported_by[shape.id].add(supported_by_id)
        return supports, supported_by

    def solve_part_2(self, data: str) -> Any:
        shapes = self._parse_shapes(data)
        supports, supported_by = self._fall(shapes)
        result = (
            seq(supports)
            .map(partial(self._how_many_would_fall, supports, supported_by))
            .sum()
        )
        return result

    def _how_many_would_fall(self, supports: dict[int, set[int]], supported_by: dict[int, set[int]],
                             shape_id: int) -> int:
        shapes = {shape_id}
        queue = deque([shape_id])
        visited = set()
        while queue:
            this_shape_id = queue.pop()
            visited.add(this_shape_id)
            for other in supports[this_shape_id]:
                if seq(supported_by[other]).map(shapes.__contains__).all() and other not in visited:
                    shapes.add(other)
                    queue.append(other)
        shapes -= {shape_id}
        result = len(shapes)
        return result


if __name__ == "__main__":
    file_path = Path(__file__)
    data_path = file_path.parents[2].joinpath("data", f"data_{file_path.name[-5:-3]}.txt")
    data = data_path.read_text()
    sut = SolverImpl()
    print(sut.solver_part_1(data))
    answer_2 = sut.solve_part_2(data)
    print(answer_2)
