
import math
import re
from dataclasses import dataclass
from enum import Enum
from functools import  partial
from pathlib import Path
from typing import Any
from functional import seq

from model.transformer import Transformer


class Condition(Enum):
    LESS = "<"
    GREATER = ">"


@dataclass
class Rule:
    left: str
    condition: Condition
    right: int
    positive_result: str


class TransformerImpl(Transformer):

    def __init__(self):
        self._workflows: dict[str, list[Rule | str]] | None = None

    def transform_1(self, data: str) -> Any:

        workflows: dict[str, list[Rule | str]] = {}
        parts_list: list[dict[str, int]] = []

        for line in data.splitlines(False):
            line = line.strip()
            if len(line) > 0:
                parts = {}
                # px{a<2006:qkq,m>2090:A,rfg}
                match = re.match(r"([a-z]+){(.*)}", line)
                if match:
                    # workflow
                    key = match.group(1)
                    workflow_str = match.group(2)
                    workflow = []
                    while match := re.match(r"([a-z]+)([<|>])([0-9]+):([a-zAR]+),?", workflow_str):
                        workflow_str = workflow_str[match.end():]
                        workflow.append(Rule(match.group(1), Condition(match.group(2)), int(match.group(3)), match.group(4)))
                    workflow.append(workflow_str)
                    workflows[key] = workflow
                else:
                    # part
                    line = line.strip("{}")
                    # x=787,m=2655,a=1222,s=2876
                    while match := re.match(r"([a-z]+)=([0-9]+),?", line):
                        line = line[match.end():]
                        parts[match.group(1)] = int(match.group(2))
                    parts_list.append(parts)

        self._workflows = workflows
        result = (
            seq(parts_list)
            .filter(partial(self._apply_workflow, "in"))
            .map(lambda d: d.values())
            .flatten()
            .sum()
        )
        return result

    def _apply_workflow(self, key: str, parts: dict[str, int]) -> bool:
        if key == "A":
            return True
        elif key == "R":
            return False

        rules: list[Rule | str] = self._workflows[key]
        for rule in rules:
            if isinstance(rule, Rule):
                left = parts[rule.left]
                right = rule.right
                match rule.condition:
                    case Condition.LESS:
                        if left < right:
                            return self._apply_workflow(rule.positive_result, parts)
                    case Condition.GREATER:
                        if left > right:
                            return self._apply_workflow(rule.positive_result, parts)
            else:
                return self._apply_workflow(rule, parts)

    def transform_2(self, data: str) -> Any:
        workflows: dict[str, list[Rule | str]] = {}
        for line in data.splitlines(False):
            line = line.strip()
            if len(line) > 0:
                parts = {}
                match = re.match(r"([a-z]+){(.*)}", line)
                if match:
                    # workflow
                    key = match.group(1)
                    workflow_str = match.group(2)
                    workflow = []
                    while match := re.match(r"([a-z]+)([<|>])([0-9]+):([a-zAR]+),?", workflow_str):
                        workflow_str = workflow_str[match.end():]
                        workflow.append(Rule(match.group(1), Condition(match.group(2)), int(match.group(3)), match.group(4)))
                    workflow.append(workflow_str)
                    workflows[key] = workflow
                else:
                    break

        self._workflows = workflows
        accepted_ranges = self._solve_2()
        result = (
            seq(accepted_ranges)
            .map(lambda d: math.prod([1+ v[1] - v[0] for v in d.values()]))
            .sum()
        )
        return result

    def _solve_2(self) -> list[dict[str, tuple[int, int]]]:
        queue = [({
            key: (1, 4000)
            for key in ("x", "m", "a", "s")
        }, "in")]
        accepted_ranges = []
        while queue:
            parts, key = queue.pop()
            match key:
                case "A":
                    accepted_ranges.append(parts)
                    continue
                case "R":
                    continue
                case _:
                    pass

            workflow = self._workflows[key]
            for i, rule in enumerate(workflow):
                if isinstance(rule, Rule):
                    low, high = parts[rule.left]
                    right = rule.right
                    match rule.condition:
                        case Condition.GREATER:
                            if low > right:
                                key = rule.positive_result
                                queue.append((parts, key))
                                break
                            elif low <= right:
                                if high > right:
                                    # split
                                    higher_range = right + 1, high
                                    queue.append((parts | {rule.left: higher_range}, rule.positive_result))
                                    # run higher range through system
                                    lower_range = low, right
                                    parts[rule.left] = lower_range
                                    # process next rule with rejected range
                                    pass
                                else:
                                    # next rule
                                    pass
                        case Condition.LESS:
                            if high < right:
                                key = rule.positive_result
                                queue.append((parts, key))
                                break
                            elif high >= right:
                                if low < right:
                                    # split
                                    lower_range = low, right - 1
                                    queue.append((parts | {rule.left: lower_range}, rule.positive_result))
                                    # run lower range through system
                                    higher_range = right, high
                                    parts[rule.left] = higher_range
                                    # process next rule with rejected range
                                    pass
                            else:
                                # next rule
                                pass
                else:
                    queue.append((parts, rule))
        return accepted_ranges


if __name__ == "__main__":
    file_path = Path(__file__)
    data_path = file_path.parents[2].joinpath("data", f"data_{file_path.name[-5:-3]}.txt")
    data = data_path.read_text()
    sut = TransformerImpl()
    print(sut.transform_1(data))
    answer_2 = sut.transform_2(data)
    print(answer_2)
