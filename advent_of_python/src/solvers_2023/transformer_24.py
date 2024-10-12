import itertools

import re
from pathlib import Path
from typing import Any

from solver import Solver


def is_counter_clockwise(a, b, c):
    return (c[1] - a[1]) * (b[0] - a[0]) > (b[1] - a[1]) * (c[0] - a[0])


def lines_intersect(a, b, c, d):
    result = (
            is_counter_clockwise(a, c, d) != is_counter_clockwise(b, c, d)
            and is_counter_clockwise(a, b, c) != is_counter_clockwise(a, b, d)
    )
    return result


class SolverImpl(Solver):
    def solver_part_1(self, data: str, min_bound: int, max_bound: int) -> Any:
        point_velocities = []
        for line in data.splitlines(False):
            line = line.strip()
            if len(line) > 0:
                # 19, 13, 30 @ -2,  1, -2
                match = re.match(r"(-?\d+),\s*(-?\d+),\s*(-?\d+)\s+@\s+(-?\d+),\s*(-?\d+),\s*(-?\d+)", line)
                point_velocities.append(
                    (
                        (int(match.group(1)), int(match.group(2))),
                        (int(match.group(4)), int(match.group(5)))
                    )
                )
        # project
        result = 0
        for (a, v), (b, w) in itertools.combinations(point_velocities, 2):
            intersection_point = self._get_intersection_point(a,v,b,w)
            if intersection_point is not None and (
                    (min_bound <= intersection_point[0] <= max_bound)
                    and (min_bound <= intersection_point[1] <= max_bound)
            ):
                result += 1
        return result

    def _get_intersection_point(self, a,v,b,w):
        # rearrange for y= mx + c
        dx, dy = v
        m1 = dy / dx
        c1 = a[1] - m1 * a[0]
        # rearrange for y= mx + c
        dx, dy = w
        m2 = dy / dx
        c2 = b[1] - m2 * b[0]
        # point where they intersect
        try:
            x = (c2 - c1) / (m1 - m2)
            y = m1 * x + c1
            # time to get there
            time1 = (x - a[0]) / v[0]
            time2 = (x - b[0]) / w[0]
            if time1 < 0 or time2 < 0:
                return None
            return round(x, 3), round(y, 3)
        except ZeroDivisionError:
            return None


    def solve_part_2(self, data: str) -> Any:
        return 0


if __name__ == "__main__":
    file_path = Path(__file__)
    data_path = file_path.parents[2].joinpath("data", f"data_{file_path.name[-5:-3]}.txt")
    data = data_path.read_text()
    sut = SolverImpl()
    print(sut.solver_part_1(data, 200000000000000, 400000000000000))
    answer_2 = sut.solve_part_2(data)
    print(answer_2)
