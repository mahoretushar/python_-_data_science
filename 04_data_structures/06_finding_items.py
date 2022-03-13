# there are times when we want to find an index of a given object in a list
letters = ["a", "b", "c", "d", "e", "d", 1, 2, 3]

# let's say that we want to find the index of letter 'a', for that:
print(letters.index(1))

# What if we try to find an item that doesn't exist
# print(letters.index("z")) # generates error

# to prevent this thing from happening, we need to check the occurrence first and then print it
# and for that we use the 'in' operator
if "z" in letters:
    print(letters.index("z"))
else:
    print("Letter not in List")

# we have another useful method that can be useful for us, i.e. 'count' which will return total number of occurrences
# of a specified item
print(f"Number of d's in Letters List: {letters.count('d')}")
