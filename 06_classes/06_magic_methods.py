class Point:
    def __init__(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def draw(self):
        print(f"Points are ({self.x}, {self.y})")


point_1 = Point(1, 2)
point_1.draw()
print(str(point_1))
