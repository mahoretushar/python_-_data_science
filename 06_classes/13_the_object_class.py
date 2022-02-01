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
print(isinstance(m, Mammal))
print(isinstance(m, Animal))
print(isinstance(m, object))

o = object()    # object class is base class of all the classes
o.__init__()

print(issubclass(Mammal, Animal))
print(issubclass(Mammal, object))
