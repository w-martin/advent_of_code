import itertools
from copy import deepcopy

from collections import defaultdict
from pathlib import Path
from typing import Any
from functional import seq

from model.transformer import Transformer


class TransformerImpl(Transformer):

    def transform_1(self, data: str, ignore_pairs: set[tuple[str, str]]=None) -> Any:
        edges: list[tuple[str, str]] = set()
        for line in data.splitlines(False):
            line = line.strip()
            if len(line) > 0:
                lhs, rhs = tuple(line.split(": "))
                for other in rhs.split():
                    edges.add(tuple(sorted([lhs, other])))

        node_connections: dict[str, set[str]] = defaultdict(set)
        for edge in edges:
            node_connections[edge[0]].add(edge[1])
            node_connections[edge[1]].add(edge[0])

        for pair in itertools.combinations(node_connections, 2):
            if pair in ignore_pairs:
                continue
            if len(paths := self._get_disjoint_paths(pair[0], pair[1], node_connections)) == 3:
                for edge_1 in paths[0]:
                    for edge_2 in paths[1]:
                        for edge_3 in paths[2]:
                            groups: list[set[str]] = []
                            for edge in edges - {edge_1, edge_2, edge_3}:
                                matches = seq(groups).filter(lambda group: seq(edge).map(group.__contains__).any()).to_list()
                                if len(matches) == 2:
                                    matches[0].update(matches[1])
                                    groups.remove(matches[1])
                                elif len(matches) == 1:
                                    matches[0].update(edge)
                                else:
                                    groups.append(set(edge))
                            if len(groups) == 2:
                                result = seq(groups).map(len).product()
                                print(f"Removed {edge_1}, {edge_2}, {edge_3} for result {result}")
                                return result

                path_sets = seq(paths).map(set).to_list()
                are_disjoint = seq(path_sets).map(
                    lambda path_set: seq(path_sets).filter(lambda other: path_set != other).map(
                        lambda other: path_set.isdisjoint(other)).all()).all()
                print(f"No edges found for {pair} to separate set. Disjoint: {are_disjoint}")
        return 0

    def _get_disjoint_paths(self, start: str, end: str, node_connections: dict[str, set[str]]) -> list[list[tuple[str, str]]]:
        paths: list[list[tuple[str, str]]] = []
        node_connections = deepcopy(node_connections)
        while (path := self._bfs(start, end, node_connections)) is not None:
            paths.append(path)
            for edge in path:
                node_connections[edge[0]] -= {edge[1]}
                node_connections[edge[1]] -= {edge[0]}
        # print(f"Found {len(paths)} paths between {start} and {end}")
        return paths

    def _bfs(self, start: str, end: str, node_connections: dict[str, set[str]]) -> list[tuple[str, str]] | None:
        max_path_len = 7
        queue = [[start]]
        while queue:
            path = queue.pop()
            if path[-1] == end:
                result = list(zip(path[:-1], path[1:]))
                return result
            if len(path) == max_path_len - 1:
                continue
            connections = node_connections[path[-1]] - set(path)
            for connection in connections:
                queue.append(path + [connection])
        return None

    def transform_2(self, data: str) -> Any:
        return 0


if __name__ == "__main__":
    file_path = Path(__file__)
    data_path = file_path.parents[2].joinpath("data", f"data_{file_path.name[-5:-3]}.txt")
    data = data_path.read_text()
    sut = TransformerImpl()
    print(sut.transform_1(data, ignore_pairs={
        ('dnz', 'kgd'),
        ('dnz', 'bxr'),
        ('dnz', 'jld'),
        ('dnz', 'zdc'),
        ('dnz', 'vfh'),
        ('dnz', 'vtr'),
        ('dnz', 'jxc'),
        ('dnz', 'rfl'),
        ('dnz', 'tdd'),
        ('dnz', 'fqj'),
        ('dnz', 'lgr'),
        ('dnz', 'rth'),
        ('dnz', 'vml'),
        ('dnz', 'xcr'),
        ('dnz', 'glf'),
        ('dnz', 'pxv'),
        ('dnz', 'xvk'),
    }))
    answer_2 = sut.transform_2(data)
    print(answer_2)
