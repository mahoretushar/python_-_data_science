class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def draw(self):
        print(f"Point({self.x}, {self.y})")


point_1 = Point(x=1, y=2)
point_1.draw()
