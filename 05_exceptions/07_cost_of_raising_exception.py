from timeit import timeit

code_1 = """
def calculate_xfactor(age):
    if age < 10:
        raise ValueError("Age cannot be 0")
    return 10 / age


try:
    calculate_xfactor(5)
except ValueError as er:
    pass
"""

code_2 = """
def calculate_xfactor(age):
    if age < 10:
        return None
    return 10 / age


xfactor = calculate_xfactor(-1)
if xfactor == None:
    pass
"""

# timeit(code_1, number=10000)
print(f"First Code: {timeit(code_1, number=10000)}")
print(f"Second Code: {timeit(code_2, number=10000)}")
