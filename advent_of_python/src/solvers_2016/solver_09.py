import re

from markdown_it.rules_inline.backticks import regex

from solver import Solver


class SolverImpl(Solver):
    _regex = re.compile("\((\d+)x(\d+)\)")

    def solve_part_1(self, data: str) -> int:
        result = ""
        next_position = 0
        for position, character in enumerate(data.strip()):
            if position < next_position:
                continue
            if character == "(":
                match = self._regex.match(data[position:])
                num_characters = int(match.group(1))
                length = int(match.group(2))
                next_position = match.end() + position + num_characters
                repeated_group = data[match.end() + position:next_position]
                result += repeated_group * length
            else:
                result += character
        print(result)
        return len(result)

    def solve_part_2(self, data: str) -> int:
        return self._decompress(data)

    def _decompress(self, data: str) -> int:
        result = 0
        next_position = 0
        for position, character in enumerate(data.strip()):
            if position < next_position:
                continue
            if character == "(":
                match = self._regex.match(data[position:])
                num_characters = int(match.group(1))
                length = int(match.group(2))
                next_position = match.end() + position + num_characters
                repeated_group = data[match.end() + position:next_position]
                result += length * self._decompress(repeated_group)
            else:
                result += 1
        return result
