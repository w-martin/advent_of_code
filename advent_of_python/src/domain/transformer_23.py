import heapq

import numpy as np

import math
from collections import defaultdict
from functools import lru_cache
from pathlib import Path
from typing import Any
from functional import seq

from model.transformer import Transformer

LEFT = (0, -1)
RIGHT = (0, 1)
UP = (-1, 0)
DOWN = (1, 0)


class TransformerImpl(Transformer):

    def _solve_1(self, arr):
        location = (0, np.where(arr[0] == ".")[0][0])
        destination = (arr.shape[0] - 1, np.where(arr[-1] == ".")[0][0])
        distances = defaultdict(lambda: math.inf)
        last_trajectory: tuple[int, int] | None = None
        loss: int = 0
        option = loss, location, last_trajectory, {location}
        queue = []
        heapq.heappush(queue, option)
        max_path = []
        while len(queue) > 0:
            loss, location, last_trajectory, path = heapq.heappop(queue)
            if location == destination:
                if len(path) > len(max_path):
                    max_path = path

            trajectories = self._get_position_trajectories(last_trajectory, location, arr)

            for new_trajectory in trajectories:
                new_loss = loss - 1
                new_location = (
                    location[0] + new_trajectory[0],
                    location[1] + new_trajectory[1]
                )
                in_bounds = (0 <= new_location[0] < arr.shape[0] and 0 <= new_location[1] < arr.shape[1])
                if in_bounds and (new_location not in path) and (arr[new_location] != "#") and new_loss < distances[
                    new_location]:
                    distances[new_location] = new_loss
                    heapq.heappush(queue, (new_loss, new_location, new_trajectory, path | {new_location}))

        result = len(max_path) - 1
        return result

    def _parse_input(self, data):
        lines = (
            seq(data.splitlines(False))
            .map(lambda line: line.strip())
            .filter(lambda line: len(line) > 0)
            .to_list()
        )
        arr = np.array([list(line) for line in lines])
        return arr

    def _get_position_trajectories(self, trajectory, position, arr):
        match arr[position]:
            case "^":
                trajectories = (UP,)
            case "v":
                trajectories = (DOWN,)
            case "<":
                trajectories = (LEFT,)
            case ">":
                trajectories = (RIGHT,)
            case "#":
                trajectories = ()
            case _:
                trajectories = self._get_trajectories(trajectory)
        return trajectories

    @lru_cache(maxsize=None)
    def _get_trajectories(self, trajectory):
        match trajectory:
            case (-1, 0):
                trajectories = (LEFT, RIGHT, UP)
            case (0, 1):
                trajectories = (UP, DOWN, RIGHT)
            case (1, 0):
                trajectories = (RIGHT, LEFT, DOWN)
            case (0, -1):
                trajectories = (DOWN, UP, LEFT)
            case _:
                trajectories = (LEFT, UP, RIGHT, DOWN)
        return trajectories

    def transform_1(self, data: str) -> Any:
        arr = self._parse_input(data)
        result = self._solve_1(arr)
        return result

    def transform_2(self, data: str) -> Any:
        for direction in ("^", "v", "<", ">"):
            data = data.replace(direction, ".")
        arr = self._parse_input(data)
        arr = arr == "."
        result = self._solve_2(arr)
        return result

    def _solve_2(self, arr: np.ndarray):
        self._arr = arr
        start = (0, np.where(arr[0])[0][0])
        end = (arr.shape[0] - 1, np.where(arr[-1])[0][0])

        neighbour_dict = {
            location: self._get_neighbours(arr, location)
            for location in zip(*np.where(arr))
        }
        pathway_points = (
            seq(neighbour_dict.items())
            .filter(lambda item: len(item[1]) == 2)
            .to_dict()
        )
        # join pathway points
        for location, neighbour_distance_map in pathway_points.items():
            neighbour_distance_list = list(neighbour_distance_map.items())
            neighbour_dict[neighbour_distance_list[0][0]][neighbour_distance_list[1][0]] = neighbour_dict[neighbour_distance_list[0][0]][location] + neighbour_distance_list[1][1]
            neighbour_dict[neighbour_distance_list[1][0]][neighbour_distance_list[0][0]] = neighbour_dict[neighbour_distance_list[1][0]][location] + neighbour_distance_list[0][1]
            del neighbour_dict[neighbour_distance_list[0][0]][location]
            del neighbour_dict[neighbour_distance_list[1][0]][location]
            del neighbour_dict[location]

        queue = [(0, start, {start})]
        max_len = 0
        while len(queue) > 0:
            loss, location, path = queue.pop()
            if location == end:
                max_len = max(max_len, loss)
            for neighbour, distance in neighbour_dict[location].items():
                if neighbour not in path:
                    queue.append((loss + distance, neighbour, path | {neighbour}))
        return max_len

    def _get_neighbours(self, arr, location) -> dict[tuple[int, int], int]:
        result = {}
        for trajectory in (UP, DOWN, LEFT, RIGHT):
            new_location = (
                location[0] + trajectory[0],
                location[1] + trajectory[1]
            )
            if (0 <= new_location[0] < arr.shape[0] and 0 <= new_location[1] < arr.shape[1]) and arr[new_location]:
                result[new_location] = 1
        return result

    @lru_cache(maxsize=None)
    def _get_options(self, location, last_trajectory) -> list[tuple[int, int]]:
        trajectories = self._get_trajectories(last_trajectory)
        result = []
        for new_trajectory in trajectories:
            new_location = (
                location[0] + new_trajectory[0],
                location[1] + new_trajectory[1]
            )
            in_bounds = (0 <= new_location[0] < self._arr.shape[0] and 0 <= new_location[1] < self._arr.shape[1])
            if in_bounds and self._arr[new_location]:
                result.append((new_location, new_trajectory))
        return result


if __name__ == "__main__":
    file_path = Path(__file__)
    data_path = file_path.parents[2].joinpath("data", f"data_{file_path.name[-5:-3]}.txt")
    data = data_path.read_text()
    sut = TransformerImpl()
    print(sut.transform_1(data))
    answer_2 = sut.transform_2(data)
    print(answer_2)
