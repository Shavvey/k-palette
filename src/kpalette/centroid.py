import numpy as np
import numpy.typing as npt
from kpalette.point import Point


class Centroid:
    """
    `Centroid` in 3D Metric space has two components:

    - The point of the centroid itself in 3D space
    - The points assigned to the centroid
    """

    points: npt.NDArray
    point: Point

    def __init__(self, max_rand: int):
        pass
