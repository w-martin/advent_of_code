from collections import defaultdict
from heapq import heappush, heappop
from typing import Any

import math
from functional import seq

from solver import Solver


class SolverImpl(Solver):

    def __init__(self):
        self._graph: dict[str, list[tuple[str, int]]] = defaultdict(list)

    def solve_part_1(self, data: str) -> Any:
        (
            seq(data.strip().splitlines(keepends=False))
            .map(str.split)
            .for_each(self._register_node)
        )
        all_nodes = set(self._graph.keys())
        q = []
        for source in self._graph.keys():
            heappush(q, (0, ({source}, source,)))
        distance: int
        visited: set[str]
        head: str
        while q:
            distance, rest = heappop(q)
            visited, head = rest
            if len(visited) == len(all_nodes):
                return distance
            for v, d in self._graph[head]:
                if v not in visited:
                    heappush(q, (distance + d, (visited.union({v}), v,)))
        return math.inf

    def _register_node(self, parts: list[str]) -> None:
        distance = int(parts[4])
        a = parts[0]
        b = parts[2]
        self._graph[a].append((b, distance))
        self._graph[b].append((a, distance))

    def solve_part_2(self, data: str) -> Any:
        (
            seq(data.strip().splitlines(keepends=False))
            .map(str.split)
            .for_each(self._register_node)
        )
        all_nodes = set(self._graph.keys())
        q = []
        for source in self._graph.keys():
            heappush(q, (0, ({source}, source,)))
        distance: int
        visited: set[str]
        head: str
        result = math.inf
        while q:
            distance, rest = heappop(q)
            visited, head = rest
            if len(visited) == len(all_nodes):
                result = min(distance, result)
            for v, d in self._graph[head]:
                if v not in visited:
                    heappush(q, (distance - d, (visited.union({v}), v,)))
        return -result
