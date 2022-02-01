class Animal:
    def __init__(self):
        print("Animal Constructor")
        self.age = 1

    def eat(self):
        print("Animal Eats")


class Mammal(Animal):
    def __init__(self):
        print("Mammal Constructor")
        self.weight = 2
        super().__init__()

    def walk(self):
        print("Mammal Walks")


m = Mammal()
print(m.age)
print(m.weight)
