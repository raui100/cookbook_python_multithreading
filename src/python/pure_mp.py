from src.lib import Point, load_sharing
from src.python import pure_sp


def process_points(points: list[Point]) -> dict[Point, float]:
    """Processes the `points` with all CPU cores"""

    return load_sharing(pure_sp.process_points, points)
