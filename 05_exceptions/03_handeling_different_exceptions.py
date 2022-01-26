# try:
#     age = int(input("Enter your Age: "))
#     xfactor = 10 / age
# except ValueError:
#     print("You didn't enter a valid age")
# except ZeroDivisionError:
#     print("You didn't enter a valid age")
# else:
#     print("No Exceptions")
#
# print("Execution Continues...")

try:
    age = int(input("Enter your Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age")
else:
    print("No Exceptions")

print("Execution Continues...")
