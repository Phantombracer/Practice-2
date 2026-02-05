import tkinter as tk
from tkinter import ttk, colorchooser
import json
import os

SETTINGS_FILE = "settings.json"

def save_color(color):
    with open(SETTINGS_FILE, "w") as f:
        json.dump({"bg_color": color}, f)

def load_color():
    if os.path.exists(SETTINGS_FILE):
        with open(SETTINGS_FILE, "r") as f:
            data = json.load(f)
            return data.get("bg_color", "white")
    return "white"

window = tk.Tk()
window.title("Програма з вкладками")
window.geometry("500x400")

bg_color = load_color()
window.configure(bg=bg_color)

notebook = ttk.Notebook(window)
notebook.pack(expand=True, fill="both")

tab_main = tk.Frame(notebook, bg=bg_color)
notebook.add(tab_main, text="Головна")

tk.Label(tab_main, text="Ім'я:", bg=bg_color).grid(row=0, column=0, padx=10, pady=10)
entry_name = tk.Entry(tab_main)
entry_name.grid(row=0, column=1, padx=10, pady=10)

tk.Label(tab_main, text="Вік:", bg=bg_color).grid(row=1, column=0, padx=10, pady=10)
entry_age = tk.Entry(tab_main)
entry_age.grid(row=1, column=1, padx=10, pady=10)

def show_info():
    name = entry_name.get()
    age = entry_age.get()
    label_info.config(text=f"Ім'я: {name}\nВік: {age}")

tk.Button(tab_main, text="Показати", command=show_info).grid(row=2, column=0, columnspan=2, pady=10)
label_info = tk.Label(tab_main, text="", bg=bg_color)
label_info.grid(row=3, column=0, columnspan=2, pady=10)

tab_settings = tk.Frame(notebook, bg=bg_color)
notebook.add(tab_settings, text="Налаштування")

def choose_color():
    color = colorchooser.askcolor()[1] 
    if color:
        window.configure(bg=color)
        tab_main.configure(bg=color)
        tab_settings.configure(bg=color)
        label_info.configure(bg=color)
        save_color(color)

tk.Button(tab_settings, text="Вибрати колір фону", command=choose_color).pack(pady=20)


tab_about = tk.Frame(notebook, bg=bg_color)
notebook.add(tab_about, text="Про програму")

about_text = "Програма розроблена студентом.\nАвтор: Олександр\nРік: 2026"
tk.Label(tab_about, text=about_text, bg=bg_color, justify="left").pack(padx=20, pady=20)

window.mainloop()