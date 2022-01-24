items = [
    ("Product-1", 10),
    ("Product-2", 9),
    ("Product-3", 12),
]

# prices_list = list(map(lambda x: x[1], items))
prices_list = [i[1] for i in items]
print(prices_list)

# filtered_list = list(filter(lambda i: i[1] >= 10, items))
filtered_list = [i for i in items if i[1] >= 10]
print(filtered_list)
