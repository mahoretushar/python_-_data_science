# numbers = [1, 2, 3]

# first = numbers[0]
# second = numbers[1]
# third = numbers[2]

# first, second, third = numbers  # no. of variables = no. of elements in list
# print(first, second, third)

numbers = [1, 2, 3, 4, 5, 6, 7, 7, 50]
# first, second, *others = numbers
# print(first, second)
# print(others)

*others, last_2, last_1 = numbers
print(last_2, last_1)
print(others)

# print(numbers[len(numbers)-2:])
