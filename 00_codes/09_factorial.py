# Program to find factorial of a given number
num = int(input("Enter a Number: "))
fact = 1
if num < 0:
    print("Factorial does not exists for -ve numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1, num + 1):
        fact += i

print(f"The factorial of {num} is {fact}")
