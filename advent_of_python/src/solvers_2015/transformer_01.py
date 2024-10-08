from math import floor
from typing import Any

from transformer import Transformer


class TransformerImpl(Transformer):

    def transform_1(self, data: str) -> Any:
        return data.count('(') - data.count(')')

    def transform_2(self, data: str) -> Any:
        floor = 0
        for i, character in enumerate(data.strip()):
            match character:
                case '(':
                    floor += 1
                case ')':
                    floor -= 1
            if floor < 0:
                return 1 + i
        return -1
