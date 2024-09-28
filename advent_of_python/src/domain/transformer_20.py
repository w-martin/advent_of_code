import numpy as np

import math
import re
from abc import abstractmethod
from collections import deque
from pathlib import Path
from typing import Any, Protocol
from functional import seq

from model.transformer import Transformer


class Module(Protocol):

    @abstractmethod
    def pulse(self, pulse: bool, source: str | None) -> list[tuple[str, str, bool]]:
        ...

    @abstractmethod
    def get_destinations(self) -> list[str]:
        ...

    @abstractmethod
    def reset_calls(self) -> None:
        ...

    @abstractmethod
    def get_calls(self) -> dict[bool, int]:
        ...


class DoesNothingModule(Module):

    def __init__(self):
        self._calls = {
            False: 0,
            True: 0
        }

    def pulse(self, pulse: bool, source: str | None) -> list[tuple[str, str, bool]]:
        self._calls[pulse] += 1
        return []

    def get_destinations(self) -> list[str]:
        pass

    def reset_calls(self) -> None:
        self._calls = {
            False: 0,
            True: 0
        }

    def get_calls(self) -> dict[bool, int]:
        return self._calls


class FlipFlop(Module):

    def __init__(self, name: str, destinations: list[str]):
        self.name = name
        self._on: bool = False
        self._destinations: list[str] = destinations
        self._calls = {
            False: 0,
            True: 0
        }

    def reset_calls(self) -> None:
        self._calls = {
            False: 0,
            True: 0
        }

    def get_calls(self) -> dict[bool, int]:
        return self._calls

    def pulse(self, pulse: bool, source: str | None) -> list[tuple[str, str, bool]]:
        self._calls[pulse] += 1
        match pulse:
            case False:
                self._on = not self._on
                pulse = self._on
                return [(self.name, destination, pulse) for destination in self._destinations]
        return []

    def get_destinations(self) -> list[str]:
        return self._destinations


class Conjunction(Module):

    def __init__(self, name: str, destinations: list[str]):
        self.name = name
        self._destinations: list[str] = destinations
        self._last_pulses: dict[str, bool] = {
        }
        self._calls = {
            False: 0,
            True: 0
        }

    def get_calls(self) -> dict[bool, int]:
        return self._calls

    def reset_calls(self) -> None:
        self._calls = {
            False: 0,
            True: 0
        }

    def add_source(self, source: str) -> None:
        self._last_pulses[source] = False

    def pulse(self, pulse: bool, source: str | None) -> list[tuple[str, str, bool]]:
        self._calls[pulse] += 1
        self._last_pulses[source] = pulse
        new_pulse = not all(self._last_pulses.values())
        return [(self.name, destination, new_pulse) for destination in self._destinations]

    def get_destinations(self) -> list[str]:
        return self._destinations


class Broadcaster(Module):

    def __init__(self, name: str, destinations: list[str]):
        self.name = name
        self._destinations: list[str] = destinations
        self._calls = {
            False: 0,
            True: 0
        }

    def get_calls(self) -> dict[bool, int]:
        return self._calls

    def reset_calls(self) -> None:
        self._calls = {
            False: 0,
            True: 0
        }

    def pulse(self, pulse: bool, source: str | None) -> list[tuple[str, str, bool]]:
        self._calls[pulse] += 1
        return [(self.name, destination, pulse) for destination in self._destinations]

    def get_destinations(self) -> list[str]:
        return self._destinations


class TransformerImpl(Transformer):

    def transform_1(self, data: str) -> Any:

        module_map: dict[str, Module] = {}
        for line in data.splitlines(False):
            line = line.strip()
            if len(line) > 0:
                # broadcaster -> a, b, c
                # %a -> b
                match line[0]:
                    case "%":
                        match = re.match(r"%([a-z]+) -> ([a-z, ]+)", line)
                        module_map[match.group(1)] = FlipFlop(match.group(1), match.group(2).split(", "))
                    case "&":
                        match = re.match(r"&([a-z]+) -> ([a-z, ]+)", line)
                        module_map[match.group(1)] = Conjunction(match.group(1), match.group(2).split(", "))
                    case _:
                        match = re.match(r"([a-z]+) -> ([a-z, ]+)", line)
                        module_map[match.group(1)] = Broadcaster(match.group(1), match.group(2).split(", "))

        for source in module_map.values():
            for destination in source.get_destinations():
                module = module_map.get(destination)
                if isinstance(module, Conjunction):
                    module.add_source(source.name)

        pulse_history: list[tuple[int, int]] = []
        num_button_presses = 1_000

        for i in range(num_button_presses):
            low = 0
            high = 0
            queue = deque([("button", "broadcaster", False)])
            while queue:
                source, dest, pulse = queue.popleft()
                # print(f"{source} -{'high' if pulse else 'low'} -> {dest}")
                match pulse:
                    case False:
                        low += 1
                    case True:
                        high += 1
                if dest in module_map:
                    queue.extend(module_map[dest].pulse(pulse, source))
            pulse_history.append((low, high))
            if repeating_pattern := self._get_repeating_pattern(pulse_history):
                break

        if len(pulse_history) != num_button_presses:
            num_project_full_range = ((num_button_presses - len(pulse_history)) // len(repeating_pattern))
            projected_history = num_project_full_range * np.vstack(repeating_pattern).sum(axis=0)
            num_extra = num_button_presses - len(pulse_history) - (num_project_full_range * len(repeating_pattern))
            if num_extra:
                projected_history += np.vstack(repeating_pattern[:num_extra]).sum(axis=0)
            result = np.vstack(pulse_history).sum(axis=0) + projected_history
            result = result.prod()
            return result
        else:
            result = np.vstack(pulse_history).sum(axis=0).prod()
            return result

    def _get_repeating_pattern(self, pulse_history: list[tuple[int, int]]) -> list[tuple[int, int]] | None:
        for i in range(2, len(pulse_history) // 2):
            if pulse_history[-i:] == pulse_history[-2 * i:-i]:
                return pulse_history[-i:]

    def transform_2(self, data: str) -> Any:

        module_map: dict[str, Module] = {}
        for line in data.splitlines(False):
            line = line.strip()
            if len(line) > 0:
                # broadcaster -> a, b, c
                # %a -> b
                match line[0]:
                    case "%":
                        match = re.match(r"%([a-z]+) -> ([a-z, ]+)", line)
                        module_map[match.group(1)] = FlipFlop(match.group(1), match.group(2).split(", "))
                    case "&":
                        match = re.match(r"&([a-z]+) -> ([a-z, ]+)", line)
                        module_map[match.group(1)] = Conjunction(match.group(1), match.group(2).split(", "))
                    case _:
                        match = re.match(r"([a-z]+) -> ([a-z, ]+)", line)
                        module_map[match.group(1)] = Broadcaster(match.group(1), match.group(2).split(", "))

        for source in module_map.values():
            for destination in source.get_destinations():
                module = module_map.get(destination)
                if isinstance(module, Conjunction):
                    module.add_source(source.name)

        i = 0
        rx_parent = (
            seq(module_map.values())
            .filter(lambda module: "rx" in module.get_destinations())
            .to_list()
        )
        rx_parent_names = seq(rx_parent).map(lambda module: module.name).to_set()
        rx_parent_earliest: dict[str, int] = {}
        num_expected = (
            seq(module_map.values())
            .count(lambda module: len(set(module.get_destinations()) & rx_parent_names) > 0)
        )

        while True:
            i += 1
            queue = deque([("button", "broadcaster", False)])
            for module in module_map.values():
                module.reset_calls()
            while queue:
                source, dest, pulse = queue.popleft()
                if dest in rx_parent_names and pulse:
                    if source not in rx_parent_earliest:
                        rx_parent_earliest[source] = i
                        print(f"{source} at {i}")
                        if len(rx_parent_earliest) == num_expected:
                            result = math.lcm(*rx_parent_earliest.values())
                            return result
                if dest in module_map:
                    queue.extend(module_map[dest].pulse(pulse, source))
                else:
                    module_map[dest] = DoesNothingModule()
                    module_map[dest].pulse(pulse, source)

            module = module_map.get("rx", None)
            # print(f"{i}: {module.get_calls()[False]}")
            if module.get_calls()[False] == 1:
                break

        return 0


if __name__ == "__main__":
    file_path = Path(__file__)
    data_path = file_path.parents[2].joinpath("data", f"data_{file_path.name[-5:-3]}.txt")
    data = data_path.read_text()
    sut = TransformerImpl()
    print(sut.transform_1(data))
    answer_2 = sut.transform_2(data)
    print(answer_2)
