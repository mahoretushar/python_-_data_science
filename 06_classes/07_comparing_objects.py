class Point:
    def __init__(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __lt__(self, other):
        return self.x < other.x and self.y < other.y


# point_1 = Point(1, 2)
# point_2 = Point(1, 2)
# print(point_1 == point_2)

point_1 = Point(1, 2)
point_2 = Point(10, 20)
print(point_1 < point_2)
print(point_1 > point_2)
