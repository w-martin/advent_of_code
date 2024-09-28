
import math
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any
from functional import seq
import numpy as np

from model.transformer import Transformer

LEFT = (0, -1)
RIGHT = (0, 1)
UP = (-1, 0)
DOWN = (1, 0)



@dataclass
class Step:
    direction: tuple[int, int]
    steps: int


class TransformerImpl(Transformer):

    def __init__(self):
        self._arr: np.ndarray | None = None

    def transform_1(self, data: str) -> Any:

        DIRECTION_MAP = {
            "U": UP,
            "D": DOWN,
            "L": LEFT,
            "R": RIGHT,
        }

        steps = []
        for line in data.splitlines(False):
            line = line.strip()
            if len(line) > 0:
                match = re.match(r"([UDLR]) (\d+) \((#[0-9a-f]{6})\)", line)
                steps.append(Step(DIRECTION_MAP[match.group(1)], int(match.group(2))))

        vertices = [(0, 0)]
        for step in steps:
            vertices.append((vertices[-1][0] + step.direction[0] * step.steps, vertices[-1][1] + step.direction[1] * step.steps))

        area = self._shoestring(vertices)
        length = seq(steps).map(lambda step: step.steps).sum()

        result = area + length // 2 + 1
        return result

    def _shoestring(self, vertices: list[tuple[int, int]]) -> int:
        result = 0
        # corners = [vertices[i] for i in range(0, len(vertices), 2)]
        for pair in zip(vertices, vertices[1:]):
            arr = np.array(pair)
            section_area = np.linalg.det(arr)
            result += section_area
        result = int(math.ceil(abs(result / 2)))
        return result

    def transform_2(self, data: str) -> Any:

        DIRECTION_MAP = {
            "3": UP,
            "1": DOWN,
            "2": LEFT,
            "0": RIGHT,
        }

        steps = []
        for line in data.splitlines(False):
            line = line.strip()
            if len(line) > 0:
                match = re.match(r"([UDLR]) (\d+) \((#[0-9a-f]{6})\)", line)
                hex_part = match.group(3)[1:]
                direction = hex_part[-1]
                n_steps = int(hex_part[:-1], 16)
                steps.append(Step(DIRECTION_MAP[direction], n_steps))

        vertices = [(0, 0)]
        for step in steps:
            vertices.append((vertices[-1][0] + step.direction[0] * step.steps, vertices[-1][1] + step.direction[1] * step.steps))

        area = self._shoestring(vertices)
        length = seq(steps).map(lambda step: step.steps).sum()

        result = area + length // 2 + 1
        return result


if __name__ == "__main__":
    file_path = Path(__file__)
    data_path = file_path.parents[2].joinpath("data", f"data_{file_path.name[-5:-3]}.txt")
    data = data_path.read_text()
    sut = TransformerImpl()
    print(sut.transform_1(data))
    answer_2 = sut.transform_2(data)
    print(answer_2)
