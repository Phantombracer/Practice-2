class Car:
    def __init__(self, brand, year, mileage):
        self.brand = brand
        self.year = year
        self.mileage = mileage

    def drive(self, km):
        if km > 0:
            self.mileage += km
        else:
            print("Пробіг не може бути від'ємним")

    def info(self):
        print(self)

    def __str__(self):
        return f"Авто: {self.brand}, рік випуску: {self.year}, пробіг: {self.mileage} км"


car1 = Car("Toyota", 2015, 120000)
car2 = Car("BMW", 2018, 80000)

car1.drive(150)
car2.drive(300)

car1.info()
car2.info()