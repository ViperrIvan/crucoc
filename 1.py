from abc import abstractmethod
class Animal:
    @abstractmethod
    def make_sound(self):
        pass

class Cat(Animal):
    def make_sound(self):
        print("Кот мяукает")

class Dog(Animal):
    def make_sound(self):
        print("Собака лает")

a = Cat
b = Dog
a.make_sound()
b.make_sound()
