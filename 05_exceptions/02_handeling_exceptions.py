# try:
#     age = int(input("Enter your Age: "))
# except ValueError:
#     print("You didn't enter a valid age")
# else:
#     print("No Exceptions")
#
# print("Execution Continues...")

try:
    age = int(input("Enter your Age: "))
    print(age)
except ValueError as ex:
    print("You didn't enter a valid age")
    print(ex)
    print(type(ex))
else:
    print("No Exceptions")

print("Execution Continues...")
