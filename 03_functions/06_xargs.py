# *args

def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print(multiply(2, 3))
print(multiply(1, 2, 3, 4))
