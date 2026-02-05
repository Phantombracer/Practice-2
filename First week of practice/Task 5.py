n = int(input("Введіть кількість елементів масиву: "))

arr = []

for i in range(n):
    value = float(input(f"Введіть елемент {i + 1}: "))
    arr.append(value)

print("\nПочатковий масив:")
print(arr)

for i in range(n):
    for j in range(0, n - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print("\nВідсортований масив:")
print(arr)