import tkinter as tk
from logic import square_number  

class App:
    def __init__(self, master):
        self.master = master
        master.title("Квадрат числа")
        master.geometry("300x150")

        tk.Label(master, text="Введіть число:").pack(pady=5)
        self.entry = tk.Entry(master)
        self.entry.pack(pady=5)

        self.result_label = tk.Label(master, text="Результат: ")
        self.result_label.pack(pady=5)

        tk.Button(master, text="Обчислити квадрат", command=self.calculate).pack(pady=5)

    def calculate(self):
        try:
            num = float(self.entry.get())
            result = square_number(num)
            self.result_label.config(text=f"Результат: {result}")
        except ValueError:
            self.result_label.config(text="Помилка: введіть число")