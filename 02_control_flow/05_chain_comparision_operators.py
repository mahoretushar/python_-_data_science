# age = 22
#
# if 18 <= age < 65:
#     print("Eligible")

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
