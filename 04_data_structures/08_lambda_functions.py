items = [
    ("Product-1", 10),
    ("Product-2", 9),
    ("Product-3", 12),
]


# def sort_items(items):
#     return items[1]
# items.sort(key=sort_items)

items.sort(key=lambda items: items[1])
print(items)
