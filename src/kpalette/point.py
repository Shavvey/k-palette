class Point:
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
