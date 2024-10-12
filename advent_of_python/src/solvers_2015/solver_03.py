from typing import Any

from solver import Solver


class SolverImpl(Solver):

    def solver_part_1(self, data: str) -> Any:
        location = (0, 0)
        visited: set[tuple[int, int]] = {location}
        for character in data:
            location = self._apply_direction(character, location)
            visited.add(location)
        return len(visited)

    def _apply_direction(self, character, location):
        match character:
            case "^":
                location = (location[0], location[1] + 1)
            case "v":
                location = (location[0], location[1] - 1)
            case ">":
                location = (location[0] + 1, location[1])
            case "<":
                location = (location[0] - 1, location[1])
        return location

    def solve_part_2(self, data: str) -> Any:
        locations = [(0, 0), (0, 0)]
        index = 0
        visited: set[tuple[int, int]] = {locations[0]}
        for character in data:
            locations[index] = self._apply_direction(character, locations[index])
            visited.add(locations[index])
            index = 1 - index
        return len(visited)
