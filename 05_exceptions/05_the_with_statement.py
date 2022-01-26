try:
    with open("01_exceptions.py") as file, open("xyz.txt") as file_2:
        print("File Opened")

    age = int(input("Enter your Age: "))  # input = a
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age")
else:
    print("No Exceptions")

print("Execution Continues...")
