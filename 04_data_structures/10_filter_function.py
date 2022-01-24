items = [
    ("Product-1", 10),
    ("Product-2", 9),
    ("Product-3", 12),
]

# def filter_function(i):
#     return i >= 10

filtered_list = list(filter(lambda i: i[1] >= 10, items))
print(filtered_list)
