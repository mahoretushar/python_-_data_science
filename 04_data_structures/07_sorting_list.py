# here we have a list in which the numbers are not in any particular order
numbers = [3, 51, 2, 8, 16]

# to sort this list we call:
# numbers.sort()

# what if we want to sort items in descending order
# for that, the sort method takes two parameters, the 'key' and 'reverse'
# 'reverse' is what we can use to change the order of the sort
# numbers.sort(reverse=True)

# in addition to 'sort' method we have a built-in function called 'sorted()'
# this function can take any iterables, so we can sort any iterable
# Unlike the 'sort' method the 'sorted()' function will not modify the original list
# print(sorted(numbers))

# 'sorted()' function also have a 'reverse' argument
print(sorted(numbers, reverse=True))

# if we try to sort the following list, then python doesn't understand it, and do anything
items = [
    ("Product-1", 10),
    ("Product-2", 9),
    ("Product-3", 12),
]


# for sorting out such kind of list we need to create a function
def sort_items(items):
    return items[1]


# while calling 'sort' method, the first parameter is 'key' and this is where we need to pass the sorting function
items.sort(key=sort_items)  # here we are not calling the function, we are simply passing the reference of the function
print(items)
