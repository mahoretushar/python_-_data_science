letters = ["a", "b", "c", "d", "e"]

# for letter in letters:
#     print(letter)

# for letter in enumerate(letters):
#     print(letter[0], letter[1])
# the above line will generate a tuple,
# and we can use unpacking with tuples also
# so the below line of code is doing the same

item = (0, "a")  # tuple
print(item[0])
print(item[1])
index, letter = item

for index, letter in enumerate(letters):
    print(index, letter)
