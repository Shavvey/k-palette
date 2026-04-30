import math as m


class Point:
    "Point in 3D Dimensional Space"

    x: int = 0
    y: int = 0
    z: int = 0

    def __init__(self, x: int, y: int, z: int):
        self.x = x
        self.y = y
        self.z = z

    def __eq__(self, other):
        if not isinstance(other, Point):
            raise TypeError(
                f"Provided type of {type(other)} does not have a defined equality with Points"
            )
        return other.x == self.x and other.y == self.x and other.z == self.z

    @staticmethod
    def distance(lhs: "Point", rhs: "Point", metric: str = "euclidean") -> float:
        match metric:
            case "euclidean":
                return m.sqrt(
                    (lhs.x - rhs.x) ** 2 + (lhs.y - rhs.y) ** 2 + (lhs.z - rhs.z) ** 2
                )
            case "manhattan":
                return (lhs.x - rhs.x) + (lhs.y - rhs.y) + (lhs.z - rhs.z)
            case _:
                raise ValueError(f"Metric {metric} is not recognized")
