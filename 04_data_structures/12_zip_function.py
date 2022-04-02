# here we have two lists, let's say we want to combine them into a single list of tuples like:
# [(1, 10), (2, 20), (3, 30)]

list_1 = [1, 2, 3]
list_2 = [10, 20, 30]

# here we cannot use 'map()' or 'filter()' or 'list comprehension', because those things works with single list
# and here we have two lists, so we need something else, and that something else is 'zip()' function

print(list(zip(list_1, list_2)))
print(list(zip("abc", list_1, list_2)))
# print(list(zip("ab", list_1, list_2)))
