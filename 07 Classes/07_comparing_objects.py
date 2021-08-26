# Comparing Objects

class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __eq__(self, other) -> bool:
        return self.x == other.x and self.y == other.y

    def __gt__(self, other) -> bool:
        return self.x > other.x and self.y > other.y


point1 = Point(1, 2)
other = Point(1, 2)
print(point1 == other)

point2 = Point(10, 20)
print(point2 > other)
print(point2 < other)
