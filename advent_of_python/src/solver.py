from abc import abstractmethod
from typing import Protocol


class Solver(Protocol):

    @abstractmethod
    def solver_part_1(self, data: str) -> int:
        ...

    @abstractmethod
    def solve_part_2(self, data: str) -> int:
        ...
