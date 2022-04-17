# Program to convert dollar to rupees

def dol_rs():
    dollars = float(input("Please enter dollars: "))
    rupees = dollars * 75
    print("Dollars: ", dollars)
    print("Rupees: ", rupees)


def euro_rs():
    euro = float(input("Please enter euros: "))
    rupees = euro * 83.76
    print("Euro: ", euro)
    print("Rupees: ", rupees)


def menu():
    print("1: Dollar to Rupees")
    print("2: Euro to Rupees")
    print("3: Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        dol_rs()
    elif choice == 2:
        euro_rs()
    elif choice == 3:
        print("Good Bye")


menu()

