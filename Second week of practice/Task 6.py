class Animal:
    def sound(self):
        print("Тварина видає звук")


class Dog(Animal):
    def sound(self):
        print("Гав!")


class Cat(Animal):
    def sound(self):
        print("Мяу!")


class Cow(Animal):
    def sound(self):
        print("Муу!")


animals = [Dog(), Cat(), Cow()]

for animal in animals:
    animal.sound()