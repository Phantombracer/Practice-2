import math

a = float(input("Введіть a: "))
b = float(input("Введіть b: "))
c = float(input("Введіть c: "))

if a == 0:
    print("Це не квадратне рівняння (a = 0)")
else:
    D = b**2 - 4*a*c
    print("Дискримінант D =", D)

    if D > 0:
        x1 = (-b + math.sqrt(D)) / (2*a)
        x2 = (-b - math.sqrt(D)) / (2*a)
        print("Рівняння має два корені:")
        print("x1 =", x1)
        print("x2 =", x2)

    elif D == 0:
        x = -b / (2*a)
        print("Рівняння має один корінь:")
        print("x =", x)

    else:
        print("Рівняння не має дійсних коренів")