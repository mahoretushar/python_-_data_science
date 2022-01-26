numbers = [1, 1, 2, 3, 4]
uniques = set(numbers)
another_set = set("Hello")
# print(uniques)
# print(another_set)
second_set = {5, 6}
# print(second_set)

first_set = set(numbers)
second_set.add(7)
second_set.remove(7)
# print(len(second_set))

print(first_set | second_set)
print(first_set & second_set)
print(first_set - second_set)
print(first_set ^ second_set)   # symmetric Diff

# sets are unordered
# we cannot use indexing

# you can check for existence
if 2 in first_set:
    print("Yes")
