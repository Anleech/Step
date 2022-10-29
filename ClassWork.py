class Integer:
    @classmethod
    def verify_coords(cls, coord):
        if not isinstance(coord, int):
            raise TypeError(f"Координата {coord} должна быть числом")

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        # return instance.__dict__[self.name]
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.verify_coords(value)
        # instance.__dict__[self.name] = value
        setattr(instance, self.name, value)


class Point3d:
    x = Integer()
    y = Integer()
    z = Integer()

    def __init__(self, a, b, c):
        self.__ = a
        self.y = b
        self.z = c

    def existence(self):
        if (self.__a + self.__b > self.__c) and (self.__a + self.__c > self.__b) and (self.__b + self.__c > self.__a):
            return "существует"
        else:
            return "не существует"

    def info(self):
        print(f"Треугольник со сторонами ({self.__a}, {self.__b}, {self.__c}) {self.existence()}")


t1 = Point3d(2.2, 5, 6)
t2 = Point3d(5, 2, 8)
t3 = Point3d(7, 3, 6)

# t1.info()
# t2.info()
# t3.info()