class Person:
    def __init__(self, name, old):
        self.__name = name
        self.__old = old

    @property
    def name(selfself):
        return self.__name

    @name.setter
    def name(selfself,n):




    @property
    def old(selfself):
        return self.__old

p1 = Person('Irina', 26)
print(p1.name)
p1.name='Igor'
del p1.name

print(p1.__dict__)
