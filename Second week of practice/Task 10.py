class Car:
    def __init__(self, brand, year, mileage):
        self.brand = brand
        self.year = year
        self.mileage = mileage

    @property
    def mileage(self):
        return self.__mileage

    @mileage.setter
    def mileage(self, value):
        if value < 0:
            raise ValueError("Пробіг не може бути від'ємним")
        self.__mileage = value

    def drive(self, km):
        if km < 0:
            raise ValueError("Кілометри не можуть бути від'ємними")
        self.__mileage += km

    def __str__(self):
        return f"{self.brand} ({self.year}), пробіг: {self.mileage} км"


car = Car("Toyota", 2018, 50000)
print(car)

car.drive(150)
print(car)