import heapq

import numpy as np

from solver import Solver


class SolverImpl(Solver):
    def solve_part_1(self, data: str) -> int:
        array = np.array([[int(li) if li.isnumeric() else -1 for li in list(line.strip())] for line in data.strip().splitlines(keepends=False)], dtype=np.int8)
        total = 0
        queue = []
        routes = set()
        for y, x in zip(*(item.tolist() for item in np.where(array == 0))):
            heapq.heappush(queue, (0, ((y, x), (y, x))))
        while len(queue) > 0:
            _, (trailhead, (y, x)) = heapq.heappop(queue)
            height = array[y, x]
            ...
            if height == 9:
                route = (trailhead, (y, x))
                if route not in routes:
                    routes.add(route)
                    total += 1
                continue
            for ny, nx in (
                (y - 1, x),
                (y + 1, x),
                (y, x - 1),
                (y, x + 1),
            ):
                if 0 <= ny < array.shape[0] and 0 <= nx < array.shape[1]:
                    new_height = array[ny, nx]
                    height_diff = new_height - height
                    if height_diff == 1:
                        heapq.heappush(queue, (-new_height, (trailhead, (ny, nx))))
        return total

    def solve_part_2(self, data: str) -> int:
        array = np.array([[int(li) if li.isnumeric() else -1 for li in list(line.strip())] for line in data.strip().splitlines(keepends=False)], dtype=np.int8)
        total = 0
        queue = []
        for y, x in zip(*(item.tolist() for item in np.where(array == 0))):
            heapq.heappush(queue, (0, (y, x)))
        while len(queue) > 0:
            _, (y, x) = heapq.heappop(queue)
            height = array[y, x]
            ...
            if height == 9:
                total += 1
                continue
            for ny, nx in (
                (y - 1, x),
                (y + 1, x),
                (y, x - 1),
                (y, x + 1),
            ):
                if 0 <= ny < array.shape[0] and 0 <= nx < array.shape[1]:
                    new_height = array[ny, nx]
                    height_diff = new_height - height
                    if height_diff == 1:
                        heapq.heappush(queue, (-new_height, (ny, nx)))
        return total
