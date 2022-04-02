# to deal with large list of numbers, we use arrays
from array import array

# the first argument in array() function is typecode, search on internet about typecode
# depending on what kind of numbers we are working, we specify the typecode in array
# 'i' = signed int, 'I' = unsigned int
numbers = array("i", [1, 2, 3])
print(type(numbers))


# numbers.append(4)
# numbers.insert()
# numbers.pop()
# numbers.remove()

# numbers[0] = 1.2

a = [1, "a", "Tushar", 10.22]
a[0] = "z"

b = (1, "a", "Tushar", 10.22)
print(b)
# b[0] = "z"

numbers = array("i", [1, 2, 3])  # similar type of data
numbers[0] = 10
