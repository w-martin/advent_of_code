from abc import abstractmethod
from typing import Protocol


class Solver(Protocol):

    @abstractmethod
    def solve_part_1(self, data: str) -> int:
        ...

    @abstractmethod
    def solve_part_2(self, data: str) -> int:
        ...
