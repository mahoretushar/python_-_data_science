# for cleaning up the resources

# try:
#     file = open("01_exceptions.py")
#     age = int(input("Enter your Age: "))    # input = a
#     xfactor = 10 / age
#     file.close()
# except (ValueError, ZeroDivisionError):
#     print("You didn't enter a valid age")
# else:
#     print("No Exceptions")
#
# print("Execution Continues...")

try:
    file = open("01_exceptions.py")
    age = int(input("Enter your Age: "))    # input = a
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age")
else:
    print("No Exceptions")
finally:
    file.close()

print("Execution Continues...")
