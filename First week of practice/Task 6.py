def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


number = int(input("Введіть невід'ємне ціле число: "))

if number < 0:
    print("Факторіал від'ємного числа не визначений")
else:
    result = factorial(number)
    print(f"{number}! =", result)