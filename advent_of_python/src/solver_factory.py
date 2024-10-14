import importlib
from functools import lru_cache
from pathlib import Path

from solver import Solver


class SolverFactory:

    @lru_cache(maxsize=25 * 10)
    def new(self, year: int, day: int) -> Solver:
        module_name = f"solvers_{year}.solver_{day:02d}"
        if (Path(__file__).parent / (module_name.replace(".", "/") + ".py")).exists():
            return importlib.import_module(module_name).SolverImpl()
        else:
            raise ValueError(f"Module {module_name} not found")
