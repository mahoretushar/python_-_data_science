class Point:
    default_color = "red"

    def __init__(self, new_x, new_y):
        self.x = new_x  # instance attributes
        self.y = new_y

    def draw(self):
        print(f"Points are ({self.x}, {self.y})")


Point.default_color = "blue"

point_1 = Point(1, 2)
# point_1.draw()
print(point_1.default_color)
print(point_1.x)
print(point_1.y)

point_2 = Point(3, 4)
# point_2.draw()
print(point_2.default_color)
print(point_2.x)
print(point_2.y)

# point_1.z = 10
# point_2.a = 20


