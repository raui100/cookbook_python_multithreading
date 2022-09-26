from typing import NamedTuple, Callable, Optional
from random import random
from multiprocessing import cpu_count
import math
import operator
from functools import reduce
from multiprocessing import Pool


class Point(NamedTuple):
    """4-D point"""
    a: float
    b: float
    c: float
    d: float

    @staticmethod
    def _build_point() -> 'Point':
        """Instantiates a single 4-D `Point` with random values"""
        return Point(random(), random(), random(), random())

    @staticmethod
    def build_points(number: int) -> list['Point']:
        """Instantiates `number` of 4-D `Points`s with random values"""
        return [Point._build_point() for _ in range(number)]

    def round(self) -> 'Point':
        """Rounds all of its points to 5 decimal place"""
        return Point(
            round(self.a, 5),
            round(self.b, 5),
            round(self.c, 5),
            round(self.d, 5),
        )


def split_data(data: list) -> list[list]:
    """Splits the data evenly in as many pieces as there are cpu cores available"""
    chunk = int(math.ceil(data.__len__() / cpu_count()))

    return [data[chunk * ind: chunk * (ind + 1)] for ind in range(cpu_count())]


def assert_eq(p1: Optional[dict[Point, float]], p2: dict[Point, float]) -> dict[Point, float]:
    """Raises exception if `p1` != `p2`"""
    if p1 is not None:
        assert {point.round() for point in p1.keys()} == {point.round() for point in p2.keys()}
        assert {round(result, 5) for result in p1.values()} == {round(result, 5) for result in p1.values()}

    return p2


def load_sharing(func: Callable, points: list[Point]) -> dict[Point, float]:
    """Shares the `points` over all CPU"""
    points: list[list[Point]] = split_data(points)  # Even load on all CPU
    with Pool() as pool:
        results: list[dict[Point, float]] = pool.map(func, points)

    return reduce(operator.ior, results, {})  # Merges all dicts to a single one
