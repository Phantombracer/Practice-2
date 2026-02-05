import math

g = 9.81

v0 = float(input("Введіть початкову швидкість (м/с): "))
angle = float(input("Введіть кут вильоту (градуси): "))

angle_rad = math.radians(angle)

v0x = v0 * math.cos(angle_rad)
v0y = v0 * math.sin(angle_rad)

time_flight = 2 * v0y / g

distance = v0x * time_flight

max_height = (v0y ** 2) / (2 * g)

print("\nРезультати:")
print("Час польоту:", round(time_flight, 2), "с")
print("Дальність польоту:", round(distance, 2), "м")
print("Максимальна висота:", round(max_height, 2), "м")

print("\nВисота снаряда по секундах:")
t = 0

while True:
    height = v0y * t - (g * t ** 2) / 2

    if height < 0:
        break

    print(f"t = {t} c → h = {round(height, 2)} м")
    t += 1