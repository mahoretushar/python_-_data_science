# age should be between 18 and 65
# age = 22
# if age >= 18 and age < 65:
#     print("Eligible")

# Above code can be written as:
# age = 22
#
# if 18 <= age < 65:
#     print("Eligible")

# Below is the solution for the question:
weight = int(input("Enter Weight: "))
command = input("(L)bs or (K)g: ").lower()

if command == "l":
    kilos = 0.45 * weight
    print(f"You are {kilos} Kilos")
elif command == "k":
    lbs = weight // 0.45
    print(f"You are {lbs} lbs")
else:
    print("Enter valid option")
