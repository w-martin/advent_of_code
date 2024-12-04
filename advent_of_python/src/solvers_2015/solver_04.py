import hashlib
from typing import Any

from solver import Solver


class SolverImpl(Solver):

    def solve_part_1(self, data: str) -> Any:
        return self._find_hash_suffix(data.strip(), 5)

    def _find_hash_suffix(self, data, num_zeroes):
        desired_prefix = "0" * num_zeroes
        suffix = 0
        while True:
            hexdigest = hashlib.md5(f"{data}{suffix}".encode("utf-8")).hexdigest()
            if hexdigest.startswith(desired_prefix):
                return suffix
            suffix += 1

    def solve_part_2(self, data: str) -> Any:
        return self._find_hash_suffix(data.strip(), 6)
