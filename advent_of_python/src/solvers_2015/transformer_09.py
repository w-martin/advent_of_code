import re
from collections import defaultdict
from heapq import heappush, heappop
from typing import Any

import math
from functional import seq

from transformer import Transformer


class TransformerImpl(Transformer):
    REGEX = re.compile(r"^(\w+) to (\w+) = (\d+)$")

    def __init__(self):
        self._graph: dict[str, list[tuple[str, int]]] = defaultdict(list)

    def transform_1(self, data: str) -> Any:
        (
            seq(data.strip().splitlines(keepends=False))
            .map(self.REGEX.match)
            .for_each(self._register_node)
        )
        all_nodes = set(self._graph.keys())
        q = []
        for source in self._graph.keys():
            heappush(q, (0, [source]))
        while q:
            distance, visited = heappop(q)
            if len(visited) == len(all_nodes):
                return distance
            head = visited[-1]
            for v, d in self._graph[head]:
                if v not in visited:
                    heappush(q, (distance + d, visited + [v]))
        return math.inf

    def _register_node(self, match: re.Match) -> None:
        distance = int(match.group(3))
        a = match.group(1)
        b = match.group(2)
        self._graph[a].append((b, distance))
        self._graph[b].append((a, distance))

    def transform_2(self, data: str) -> Any:
        (
            seq(data.strip().splitlines(keepends=False))
            .map(self.REGEX.match)
            .for_each(self._register_node)
        )
        all_nodes = set(self._graph.keys())
        q = []
        for source in self._graph.keys():
            heappush(q, (0, [source]))
        while q:
            distance, visited = heappop(q)
            if len(visited) == len(all_nodes):
                return -distance
            head = visited[-1]
            for v, d in self._graph[head]:
                if v not in visited:
                    heappush(q, (distance - d, visited + [v]))
        return math.inf
