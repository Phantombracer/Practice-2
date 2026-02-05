import math

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


w = float(input("Введіть ширину прямокутника: "))
h = float(input("Введіть висоту прямокутника: "))
r = float(input("Введіть радіус кола: "))

rectangle = Rectangle(w, h)
circle = Circle(r)

print("Площа прямокутника:", rectangle.area())
print("Площа кола:", circle.area())