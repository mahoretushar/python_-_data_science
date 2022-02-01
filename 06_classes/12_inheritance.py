# class Mammal:
#     def eat(self):
#         print("Mammal Eats")
#
#     def walk(self):
#         print("Mammal Walks")
#
#
# class Fish:
#     def eat(self):
#         print("Fish Eats")
#
#     def swim(self):
#         print("Fish Swims")

class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print("Animal Eats")


class Mammal(Animal):
    def walk(self):
        print("Mammal Walks")


class Fish(Animal):
    def swim(self):
        print("Fish Swims")


m = Mammal()
m.eat()
m.walk()

f = Fish()
f.eat()
f.swim()

print(m.age)
print(f.age)









