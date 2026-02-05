import tkinter as tk

def add():
    try:
        result = float(entry1.get()) + float(entry2.get())
        label_result.config(text=f"Результат: {result}")
    except ValueError:
        label_result.config(text="Помилка: введіть числа")

def subtract():
    try:
        result = float(entry1.get()) - float(entry2.get())
        label_result.config(text=f"Результат: {result}")
    except ValueError:
        label_result.config(text="Помилка: введіть числа")

def multiply():
    try:
        result = float(entry1.get()) * float(entry2.get())
        label_result.config(text=f"Результат: {result}")
    except ValueError:
        label_result.config(text="Помилка: введіть числа")

def divide():
    try:
        denominator = float(entry2.get())
        if denominator == 0:
            label_result.config(text="Помилка: ділення на нуль")
            return
        result = float(entry1.get()) / denominator
        label_result.config(text=f"Результат: {result}")
    except ValueError:
        label_result.config(text="Помилка: введіть числа")

window = tk.Tk()
window.title("Калькулятор")
window.geometry("400x250")

tk.Label(window, text="Число 1:").grid(row=0, column=0, padx=10, pady=5)
entry1 = tk.Entry(window)
entry1.grid(row=0, column=1, padx=10, pady=5)

tk.Label(window, text="Число 2:").grid(row=1, column=0, padx=10, pady=5)
entry2 = tk.Entry(window)
entry2.grid(row=1, column=1, padx=10, pady=5)

tk.Button(window, text="+", width=5, command=add).grid(row=2, column=0, pady=10)
tk.Button(window, text="-", width=5, command=subtract).grid(row=2, column=1, pady=10)
tk.Button(window, text="*", width=5, command=multiply).grid(row=3, column=0, pady=10)
tk.Button(window, text="/", width=5, command=divide).grid(row=3, column=1, pady=10)

label_result = tk.Label(window, text="Результат: ", font=("Arial", 14))
label_result.grid(row=4, column=0, columnspan=2, pady=20)

window.mainloop()