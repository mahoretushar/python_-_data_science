# class Employee:
#     def greet(self):
#         print("Hello XXX")
#
#
# class Person:
#     def greet(self):
#         print("Hello XXX")
#
#
# # multiple inheritance
# class Manager(Employee, Person):
#     pass
#
#
# m = Manager()
# m.greet()

class Flyer:
    def fly(self):
        pass


class Swimmer:
    def swim(self):
        pass


class FlyingFish(Flyer, Swimmer):
    pass

