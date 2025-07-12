from collections import defaultdict

from functional import seq

from solver import Solver


class SolverImpl(Solver):

    def solve_part_1(self, data: str) -> int:
        data = data.strip()
        rules = defaultdict(set)
        rules_section = True
        total = 0
        for line in data.splitlines():
            if len(line) == 0:
                rules_section = False
                continue
            if rules_section:
                parts = seq(line.split("|")).map(int).to_list()
                rules[parts[1]].add(parts[0])
            else:
                parts = seq(line.split(",")).map(int).to_list()
                if self._is_valid(parts, rules):
                    total += parts[len(parts) // 2]
        return total


    def solve_part_2(self, data: str) -> int:
        data = data.strip()
        rules = defaultdict(set)
        rules_section = True
        incorrectly_ordered = []
        for line in data.splitlines():
            if len(line) == 0:
                rules_section = False
                continue
            if rules_section:
                parts = seq(line.split("|")).map(int).to_list()
                rules[parts[1]].add(parts[0])
            else:
                parts = seq(line.split(",")).map(int).to_list()
                if not self._is_valid(parts, rules):
                    incorrectly_ordered.append(parts)
        total = 0
        for parts in incorrectly_ordered:
            parts = self.sort_by_rules(parts, rules)
            total += parts[len(parts) // 2]
        return total

    def _is_valid(self, parts, rules):
        before = set()
        valid = True
        for part in parts:
            must_come_after = rules[part]
            intersection = must_come_after.intersection(parts)
            if not intersection.issubset(before):
                valid = False
                break
            before.add(part)
        return valid

    def sort_by_rules(self, unsorted_parts: list[int], rules: dict[int, set[int]]):
        sorted_parts = []
        while len(unsorted_parts) > 0:
            u = unsorted_parts.pop()
            inserted = False
            for i, p in enumerate(sorted_parts):
                if p in rules and u in rules[p]:
                    sorted_parts.insert(i, u)
                    inserted = True
                    break
            if not inserted:
                sorted_parts.append(u)
        return sorted_parts
