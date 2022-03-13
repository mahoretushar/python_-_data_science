letters = ["a", "b", "c", "d", "e"]

# adding
letters.append("z")
letters.insert(0, "-")
print(letters)

# remove
# letters.pop() # pops the last element from the list
# letters.pop(0)    # you can pass index also with pop

# if you want to remove an object but don't know the index then we can use 'remove'
letters.remove('b')  # Removes first occurrence of the letter 'b'
# if you have multiple 'b' then you have to loop over the list and remove them

# we have another way to remove an item i.e. by using 'del'
del letters[0]
# we can delete the range of items, and this is the difference between the 'pop' and 'delete'
del letters[:3]

# finally, if you want to remove all the items in the list then you can use 'clear' method
letters.clear()
print(letters)
