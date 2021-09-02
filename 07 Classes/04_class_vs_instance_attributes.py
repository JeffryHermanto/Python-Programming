# Class vs Instance Attributes

class Point:
    default_color = "red"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


point = Point(1, 2)
print(Point.default_color)
print(point.default_color)
point.draw()

another = Point(3, 4)
print(another.default_color)
another.draw()

Point.default_color = "yellow"
print(point.default_color)
print(another.default_color)
