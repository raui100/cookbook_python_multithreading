from src.lib import Point
from src.lib import split_data


def test_lib():
    def _count(data: list[list[Point]]) -> int:
        """Counts the number of total elements"""
        return sum((len(sublist) for sublist in data))

    assert _count(split_data(Point.build_points(10))) == 10  # Even
    assert _count(split_data(Point.build_points(11))) == 11  # Uneven
