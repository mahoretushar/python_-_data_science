def calculate_xfactor(age):
    if age < 10:
        raise ValueError("Age cannot be 0")
    return 10 / age


try:
    calculate_xfactor(5)
except ValueError as er:
    print(er)
