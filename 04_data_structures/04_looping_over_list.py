letters = ["a", "b", "c", "d", "e"]

# for letter in letters:
#     print(letter)

# for letter in enumerate(letters):
#     print(letter[0], letter[1])

item = (0, "a")  # tuple
print(item[0])
print(item[1])
index, letter = item

for index, letter in enumerate(letters):
    print(index, letter)
