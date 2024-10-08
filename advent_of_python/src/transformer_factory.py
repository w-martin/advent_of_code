import importlib
from functools import lru_cache
from pathlib import Path

from transformer import Transformer


class TransformerFactory:

    @lru_cache(maxsize=25 * 10)
    def new(self, year: int, day: int) -> Transformer:
        module_name = f"solvers_{year}.transformer_{day:02d}"
        if (Path(__file__).parent / (module_name.replace(".", "/") + ".py")).exists():
            return importlib.import_module(module_name).TransformerImpl()
        else:
            raise ValueError(f"Module {module_name} not found")
