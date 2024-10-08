from abc import abstractmethod
from typing import Protocol

from typing_extensions import TypeVar

T = TypeVar("T")

class Factory(Protocol[T]):
    @abstractmethod
    def new(self, identifier: str) -> T:
        ...
