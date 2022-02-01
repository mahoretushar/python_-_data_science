class Point:
    def __init__(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)


point_1 = Point(1, 2)
point_2 = Point(10, 20)
addition = point_1 + point_2
print(addition.x)
print(addition.y)
