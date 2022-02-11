# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __eq__(self, other):
#         return self.x == other.x and self.y == other.y
#
#
# p1 = Point(2, 3)
# p2 = Point(2, 3)
# print(p1 == p2)


from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p1 = Point(x=2, y=3)
p2 = Point(x=2, y=3)
print(p1 == p2)
