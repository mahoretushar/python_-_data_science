numbers = [3, 51, 2, 8, 16]
# numbers.sort()
# numbers.sort(reverse=True)

# print(sorted(numbers))
print(sorted(numbers, reverse=True))

items = [
    ("Product-1", 10),
    ("Product-2", 9),
    ("Product-3", 12),
]


def sort_items(items):
    return items[1]


items.sort(key=sort_items)
print(items)
