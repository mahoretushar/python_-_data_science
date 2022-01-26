# key, value pair
# point = {"x": 1, "y": 2}

# can use dict()
point = dict(x=1, y=2)
# print(point["y"])
point["x"] = 10
point["z"] = 50  # adding new key, value
# print(point)
# print(point["p"])

if "p" in point:
    print(point["p"])

# print(point.get("p", 0))

# del point["z"]
# print(point)

for x in point:
    print(x)

# for x in point:
#     print(x, point[x])

# for x in point.items():
#     print(x)

for key, value in point.items():
    print(key, value)
