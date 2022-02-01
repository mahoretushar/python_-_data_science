class Point:
    def __init__(self, new_x, new_y):
        self.x = new_x  # instance attributes
        self.y = new_y

    @classmethod    # decorator
    def zero(cls):
        return cls(0, 0)

    def draw(self):
        print(f"Points are ({self.x}, {self.y})")


point_1 = Point(1, 2)
point_1.draw()

point_2 = Point.zero()
point_2.draw()


