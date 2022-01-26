class Point:
    def __init__(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def draw(self):
        print(f"Points are ({self.x}, {self.y})")


point_1 = Point(1, 2)   # point_1 = 2FA64 - 2FA32
point_1.draw()
# print(point_1.x)
