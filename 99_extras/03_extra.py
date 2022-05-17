# Program to show the use of decorators
def div(x, y):
    return x / y


def my_decorator(func):
    def wrapper(x, y):
        if x < y:
            x, y = y, x
        return func(x, y)

    return wrapper


@my_decorator
def div(x, y):
    return x / y


print(div(2, 10))
