# Program to find the largest among three numbers
number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))
number_3 = int(input("Enter third number: "))

if number_1 > number_2 and number_1 > number_3:
    print("Largest number is: ", number_1)
elif number_2 > number_1 and number_2 > number_3:
    print("Largest number is: ", number_2)
else:
    print("Largest number is: ", number_3)
