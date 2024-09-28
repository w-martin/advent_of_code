from pathlib import Path
from typing import Any

from functional import seq

from model.transformer import Transformer


class TransformerImpl(Transformer):
    def _compute_line_1(self, line: str):
        result = ""
        for c in line:
            if c.isnumeric():
                result += c
                break
        for c in line[::-1]:
            if c.isnumeric():
                result += c
                break
        return int(result)

    def _compute_line_2(self, line: str):
        digit_dict = dict(zip(("one", "two", "three", "four", "five", "six", "seven", "eight", "nine"), range(1, 10)))
        digit_dict.update(zip(map(str, range(1, 10)), range(1, 10)))
        result = str(digit_dict[seq(digit_dict).filter(line.__contains__).min_by(line.index)])
        result += str(digit_dict[seq(digit_dict).filter(line.__contains__).max_by(line.rindex)])
        return int(result)

    def transform_1(self, data: str) -> Any:
        return (
            seq(data.splitlines(keepends=False))
            .map(self._compute_line_1)
            .sum()
        )

    def transform_2(self, data: str) -> Any:
        return (
            seq(data.splitlines(keepends=False))
            .map(self._compute_line_2)
            .sum()
        )


if __name__ == "__main__":
    file_path = Path(__file__)
    data_path = file_path.parents[3].joinpath("data", f"day_{file_path.name[-5:-3]}.txt")
    data = data_path.read_text()
    sut = TransformerImpl()
    print(sut.transform_1(data))
    print(sut.transform_2(data))
