import math

def rectangle_area(width, height):
    return width * height

def circle_area(radius):
    return math.pi * radius ** 2


w = float(input("Введіть ширину прямокутника: "))
h = float(input("Введіть висоту прямокутника: "))
r = float(input("Введіть радіус кола: "))

rect_area = rectangle_area(w, h)
circ_area = circle_area(r)

print("Площа прямокутника:", rect_area)
print("Площа кола:", circ_area)