students = {}
all_unique_grades = set()

n = int(input("Введіть кількість студентів: "))

for i in range(n):
    name = input("\nВведіть ім'я студента: ")

    grades_input = input("Введіть оцінки через пробіл: ")
    grades_list = list(map(int, grades_input.split()))

    average = sum(grades_list) / len(grades_list)

    students[name] = average

    unique_grades = set(grades_list)
    all_unique_grades.update(unique_grades)

    print("Середній бал студента:", average)
    print("Унікальні оцінки студента:", unique_grades)

print("\nСловник {ім'я: середній бал}:")
print(students)

print("\nУсі унікальні оцінки:", all_unique_grades)