SUBJECTS_COUNT = 5

n = int(input("Введіть кількість студентів: "))

students = []

for i in range(n):
    print(f"\nСтудент {i + 1}")
    name = input("Ім'я: ")
    surname = input("Прізвище: ")

    grades = []
    for j in range(SUBJECTS_COUNT):
        grade = float(input(f"Оцінка з дисципліни {j + 1}: "))
        grades.append(grade)

    students.append({
        "name": name,
        "surname": surname,
        "grades": grades
    })

print("\nТаблиця студентів:")
print("Ім'я\tПрізвище\tСередній бал")

for student in students:
    avg_grade = sum(student["grades"]) / SUBJECTS_COUNT
    print(f"{student['name']}\t{student['surname']}\t{round(avg_grade, 2)}")

print("\nСередній бал групи з дисциплін:")

for subject_index in range(SUBJECTS_COUNT):
    total = 0
    for student in students:
        total += student["grades"][subject_index]

    subject_avg = total / n
    print(f"Дисципліна {subject_index + 1}: {round(subject_avg, 2)}")