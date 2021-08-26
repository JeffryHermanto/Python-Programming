# Creating Classes

class Point:
    def draw(self):
        print("draw")


point = Point()
point.draw()
print(type(point))
print(isinstance(point, Point))
