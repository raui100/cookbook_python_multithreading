from src.lib import Point
import rust_lib


def process_points(points: list[Point]) -> dict[Point, float]:
    """Applies `calc` on all `Point`s in `points`. CPU bound mocking"""
    results = rust_lib.process_points(points)

    return {point: result for point, result in zip(points, results)}
