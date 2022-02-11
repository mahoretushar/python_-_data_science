class Text(str):
    def duplicate(self):
        return self + self


text_1 = Text("Hello")
print(text_1.lower())
print(text_1.upper())
print(text_1.duplicate())


class List(list):
    def append(self, object):
        print("Appending to list")
        super().append(object)


list_1 = List([1, 2, 3])
list_1.append(4)
print(list_1)
