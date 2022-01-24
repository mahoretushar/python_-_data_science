# read only list
point = (1, 2)
point = 1, 2
point = 1,
point = (1, 2) + (3, 4)
point = (1, 2) * 3

point = tuple([1, 2])
point = tuple("Hello World")
print(point)
# point[1] = "z"    # it will generate error
print(point[0:3])

point = (1, 2, 3)
x, y, z = point

if 10 in point:
    print("exists")

# [0 0 0 0 0 0 0 0] = 255
