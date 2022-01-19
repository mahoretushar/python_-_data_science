letters = ["a", "b", "c", "d", "e"]

# adding
letters.append("z")
letters.insert(0, "-")
print(letters)

# remove
# letters.pop()
# letters.pop(0)
del letters[0]
del letters[:3]
letters.clear()
print(letters)


