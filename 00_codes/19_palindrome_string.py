# Program to check if a string is palindrome or not
string = input("Enter a string: ")
if string == string[::-1]:
    print("The string is palindrome")
else:
    print("The string is not palindrome")
