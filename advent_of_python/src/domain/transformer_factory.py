import importlib
from functools import lru_cache

from model.factory import Factory
from model.transformer import Transformer


class TransformerFactory(Factory[Transformer]):

    @lru_cache(maxsize=25)
    def new(self, identifier: str) -> Transformer:
        if not (
                identifier.isnumeric() and
                1 <= int(identifier) <= 25
        ):
            raise ValueError(f"Invalid transformer id: {identifier}")

        return importlib.import_module(f"domain.transformer_{identifier}", ).TransformerImpl()
