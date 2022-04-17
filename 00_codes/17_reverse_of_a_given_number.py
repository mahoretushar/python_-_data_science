# program to find the reverse of a given number

number = int(input("Enter a number: "))
reverse = 0
while number > 0:
    remainder = number % 10
    reverse = (reverse * 10) + remainder
    number = number // 10
print("Reverse of the given number is: ", reverse)
