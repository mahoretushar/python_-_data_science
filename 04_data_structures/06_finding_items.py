letters = ["a", "b", "c", "d", "e", "d", 1, 2, 3]

print(letters.index(1))
# print(letters.index("z")) # generates error

if "z" in letters:
    print(letters.index("z"))
else:
    print("Letter not in List")

print(f"Number of d's in Letters List: {letters.count('d')}")
