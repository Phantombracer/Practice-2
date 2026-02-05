class BankAccount:
    def __init__(self, balance=0):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Поповнення на {amount} грн")
        else:
            print("Сума поповнення має бути додатною")

    def withdraw(self, amount):
        if amount <= 0:
            print("Сума зняття має бути додатною")
        elif amount > self.__balance:
            print("Недостатньо коштів")
        else:
            self.__balance -= amount
            print(f"Знято {amount} грн")

    def get_balance(self):
        return self.__balance


account = BankAccount(1000)

account.deposit(500)
account.withdraw(300)

print("Поточний баланс:", account.get_balance())