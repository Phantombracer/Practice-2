class Student:
    def __init__(self, name, group, average_grade):
        self.name = name
        self.group = group
        self.average_grade = average_grade

    def show_info(self):
        print("Ім'я:", self.name)
        print("Група:", self.group)
        print("Середній бал:", self.average_grade)
        print("-" * 30)


student1 = Student("Іван", "КН-21", 89.5)
student2 = Student("Олена", "КН-21", 92.3)
student3 = Student("Андрій", "КН-22", 85.0)

student1.show_info()
student2.show_info()
student3.show_info()