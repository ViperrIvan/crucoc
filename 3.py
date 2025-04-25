from abc import abstractmethod
class Figure:
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def calculate_square(self):
        pass
class Rectangle:
    def __init__(self, a, b):
        self.__a = a
        self.__b = b

    def calculate_square(self):
        return   self.__a * self.__b

class Square:
    def __init__(self, a):
        self.__a = a

    def calculate_square(self):
        return   self.__a * self.__a
rectangle = Rectangle(4, 5)
square = Square(5)
print(rectangle.calculate_square())
print(square.calculate_square())
