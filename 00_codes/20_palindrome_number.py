# Program to check if a number is palindrome or not
number = int(input("Enter a number: "))
temp = number
reverse = 0

while number > 0:
    remainder = number % 10
    reverse = reverse * 10 + remainder
    number = number // 10

if temp == reverse:
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")
