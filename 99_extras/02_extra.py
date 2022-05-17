class Sample:
    x = 2

    def get(self, y):
        self.y = y


s1 = Sample()
s1.get(3)
print(s1.x, " ", s1.y)
s2 = Sample()
s2.y = 4
print(s2.x, " ", s2.y)
s2.x = 5
print(s1.x, " ", s1.y)
print(s2.x, " ", s2.y)