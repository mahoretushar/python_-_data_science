items = [
    ("Product-1", 10),
    ("Product-2", 9),
    ("Product-3", 12),
]

# prices = []
# for x in items:
#     prices.append(x[1])
#
# print(prices)

var_y = list(map(lambda x: x[1], items))
# x = ("Product-1", 10) return x[1] = 10
# x = ("Product-2", 9) return x[1] = 9
# x = ("Product-3", 12) return x[1] = 12
# list(10, 9, 12) = [10, 9, 12]

print(var_y)
