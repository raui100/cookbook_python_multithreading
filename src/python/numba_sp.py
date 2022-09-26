import numba
import numpy as np
from numba.typed import List

from src.lib import Point


def process_points(points: list[Point]) -> dict[Point, float]:
    """Applies `calc` on all `Point`s in `points`. CPU bound mocking"""
    numba_points = List()
    [numba_points.append(point) for point in points]
    results = _process_points(numba_points)

    return {point: result for point, result in zip(points, results)}


@numba.njit(cache=True)
def _process_points(points: List[Point]) -> List[float]:
    """Applies `calc` on all `Point`s in `points`. CPU bound mocking"""
    results = np.zeros(len(points))
    for ind in numba.prange(len(points)):
        point = points[ind]
        results[ind] = calc(point)

    return results


@numba.njit
def calc(point: Point) -> float:
    """Mocks a CPU intensive operation with `Point`"""
    total = 0.0
    for ind in range(1, 1_000):
        total += (point.a ** 2 + point.b ** 2 + point.c ** 2 + point.d ** 2) ** 0.5 / ind

    return total

