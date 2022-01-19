message = "z"


# def greet():
#     message = "a"

def greet(name):
    print(name)
    global message
    message = "a"


greet("Bruce")
print(message)
