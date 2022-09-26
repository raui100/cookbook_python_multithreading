from src.lib import Point


def process_points(points: list[Point]) -> dict[Point, float]:
    """Applies `calc` on all `Point`s in `points`. CPU bound mocking"""
    return {point: result for point, result in (calc(point) for point in points)}


def calc(point: Point) -> tuple[Point, float]:
    """Mocks a CPU intensive operation with `Point`"""
    total = 0
    for ind in range(1, 1_000):
        total += (point.a ** 2 + point.b ** 2 + point.c ** 2 + point.d ** 2) ** 0.5 / ind

    return point, total

