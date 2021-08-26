# Class vs Instance Attributes

class Point:
    defaultColor = "red"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


point = Point(1, 2)
print(Point.defaultColor)
print(point.defaultColor)
point.draw()

another = Point(3, 4)
print(another.defaultColor)
another.draw()

Point.defaultColor = "yellow"
print(point.defaultColor)
print(another.defaultColor)
