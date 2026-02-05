import tkinter as tk

window = tk.Tk()
window.title("Анкета користувача")
window.geometry("400x300")

tk.Label(window, text="Ім'я:").grid(row=0, column=0, sticky="w", padx=10, pady=5)
entry_name = tk.Entry(window)
entry_name.grid(row=0, column=1, padx=10, pady=5)

tk.Label(window, text="Стать:").grid(row=1, column=0, sticky="w", padx=10, pady=5)
gender_var = tk.StringVar(value="Чоловіча")
tk.Radiobutton(window, text="Чоловіча", variable=gender_var, value="Чоловіча").grid(row=1, column=1, sticky="w")
tk.Radiobutton(window, text="Жіноча", variable=gender_var, value="Жіноча").grid(row=1, column=2, sticky="w")

agree_var = tk.BooleanVar()
tk.Checkbutton(window, text="Погоджуюсь із умовами", variable=agree_var).grid(row=2, column=0, columnspan=2, sticky="w", padx=10, pady=5)

def save_data():
    name = entry_name.get()
    gender = gender_var.get()
    agree = "Погоджуюсь" if agree_var.get() else "Не погоджуюсь"
    result_text = f"Ім'я: {name}\nСтать: {gender}\nПоложення: {agree}"
    label_result.config(text=result_text)

tk.Button(window, text="Зберегти", command=save_data).grid(row=3, column=0, columnspan=3, pady=10)

label_result = tk.Label(window, text="", justify="left", font=("Arial", 12))
label_result.grid(row=4, column=0, columnspan=3, padx=10, pady=10)

window.mainloop()