numbers = [1, 2, 3]
print(numbers)
print(*numbers)

first = [1, 2]
second = [3, 4, 5]

values = [*first, *"Hello", *second]
print(values)

first = {"x": 1}
second = {"y": 2, "z": 3}

combined = {**first, **second}
print(combined)
