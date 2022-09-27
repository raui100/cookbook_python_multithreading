import numpy as np
import numba as nb
from numba.typed import List

from src.lib import Point


def process_points(points: list[Point]) -> dict[Point, float]:
    """Applies `calc` on all `Point`s in `points`. CPU bound mocking"""
    # Creates a list that is usable within numba
    numba_points = List()
    [numba_points.append(point) for point in points]
    results = _process_points(numba_points)

    return {point: result for point, result in zip(points, results)}


@nb.njit(cache=True)
def _process_points(points: List[Point]) -> np.ndarray:
    matrix = np.zeros((4, len(points)), dtype=np.float64)
    for ind in range(len(points)):
        point = points[ind]
        matrix[0][ind] = point[0]
        matrix[1][ind] = point[1]
        matrix[2][ind] = point[2]
        matrix[3][ind] = point[3]

    return calc(matrix)


@nb.njit(cache=True, parallel=True)
def calc(matrix: np.ndarray) -> np.ndarray:
    """Mocks a CPU intensive operation with `Point`"""
    matrix = matrix ** 2  # Square of each element
    array = np.sum(matrix, 0)  # Sum alongside the 0 axis (eg: [[1, 1], [0, 0]] -> [1, 1]
    array = array ** 0.5  # Square root of each element

    results: np.ndarray = np.zeros(len(array), dtype=np.float64)
    for result_ind in nb.prange(len(array)):
        number = array[result_ind]
        total = 0
        for ind in range(1, 1_000):  # Mocking a real task
            total += number / ind
        results[result_ind] = total

    return results

