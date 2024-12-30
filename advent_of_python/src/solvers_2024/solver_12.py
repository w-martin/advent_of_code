import math
import numpy as np
from sklearn.preprocessing import LabelEncoder

from solver import Solver


class SolverImpl(Solver):

    def solve_part_1(self, data: str) -> int:
        array = np.array([list(line.strip()) for line in data.strip().splitlines(keepends=False)])
        label_encoder = LabelEncoder()
        array = label_encoder.fit_transform(array.reshape(-1)).reshape(array.shape)
        perimeter_template = np.zeros(shape=(array.shape[0] + 2, array.shape[1] + 2), dtype=bool)
        visited = np.zeros_like(array, dtype=bool)
        areas = []
        perimeters = []
        while visited.sum() < math.prod(array.shape):
            coordinate = np.argwhere(~visited)[0]
            new_region = self._find_region(array, coordinate)
            for coordinate in new_region:
                visited[coordinate] = True
            areas.append(len(new_region))
            new_perimeter = self._find_perimeter(new_region, perimeter_template.copy())
            perimeters.append(new_perimeter)
            ...

        return sum(area * perimeter for area, perimeter in zip(areas, perimeters))

    def solve_part_2(self, data: str) -> int:
        array = np.array([list(line.strip()) for line in data.strip().splitlines(keepends=False)])
        label_encoder = LabelEncoder()
        array = label_encoder.fit_transform(array.reshape(-1)).reshape(array.shape)
        perimeter_template = np.zeros(shape=(array.shape[0] + 2, array.shape[1] + 2), dtype=bool)
        visited = np.zeros_like(array, dtype=bool)
        areas = []
        num_sides_list = []
        while visited.sum() < math.prod(array.shape):
            coordinate = np.argwhere(~visited)[0]
            new_region = self._find_region(array, coordinate)
            for coordinate in new_region:
                visited[coordinate] = True
            areas.append(len(new_region))
            num_sides = self._find_num_sides(new_region, perimeter_template.copy())
            num_sides_list.append(num_sides)
            ...

        return sum(area * perimeter for area, perimeter in zip(areas, num_sides_list))

    def _find_region(self, array: np.ndarray, coordinate: np.ndarray):
        visited = np.zeros_like(array, dtype=bool)
        region = []
        value = array[coordinate[0], coordinate[1]]
        q = [(coordinate[0], coordinate[1])]
        while q:
            coordinate = q.pop()
            this_value = array[coordinate]
            was_visited = visited[coordinate]
            visited[coordinate] = True
            if this_value == value and not was_visited:
                region.append(coordinate)
                for new_coordinate in (
                        (coordinate[0] - 1, coordinate[1]),
                        (coordinate[0] + 1, coordinate[1]),
                        (coordinate[0], coordinate[1] - 1),
                        (coordinate[0], coordinate[1] + 1),
                ):
                    j, i = new_coordinate
                    if 0 <= i < array.shape[1] and 0 <= j < array.shape[0] and not visited[j, i]:
                        q.append(new_coordinate)
        return region

    def _find_perimeter(self, coordinates: np.ndarray, visited: np.ndarray) -> int:
        perimeter = 0
        q = []
        for j, i in coordinates:
            j += 1
            i += 1
            q.append((j - 1, i))
            q.append((j + 1, i))
            q.append((j, i - 1))
            q.append((j, i + 1))
            visited[j, i] = True
        while q:
            coordinate = q.pop()
            if not visited[coordinate]:
                perimeter += 1
        return perimeter

    def _find_num_sides(self, coordinates: np.ndarray, array: np.ndarray):
        for j, i in coordinates:
            array[j + 1, i + 1] = True

        a = array.repeat(2, axis=0).repeat(2, axis=1)
        num_sides = int(np.abs(np.diff(np.diff(a.astype(int), axis=0), axis=1)).sum())

        return num_sides
