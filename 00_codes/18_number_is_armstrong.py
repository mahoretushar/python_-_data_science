# Program to find if a number is an Armstrong number or not

number = int(input("Enter a number: "))
num = number
sum = 0

while number > 0:
    digit = number % 10
    sum += digit ** 3
    number //= 10

if num == sum:
    print("The number is an Armstrong number")
else:
    print("The number is not an Armstrong number")
