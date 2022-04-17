# Program to find factorial of a Number

def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)


print(fact(0))
print(fact(4))
