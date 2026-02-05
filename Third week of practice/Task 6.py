import tkinter as tk
from tkinter import filedialog, messagebox

window = tk.Tk()
window.title("Блокнот")
window.geometry("600x400")

current_file = None
text_changed = False

text_area = tk.Text(window, wrap="word")
text_area.pack(expand=True, fill="both")

def new_file():
    global current_file, text_changed
    if text_changed:
        if not ask_save_changes():
            return
    text_area.delete(1.0, tk.END)
    current_file = None
    text_changed = False

def open_file():
    global current_file, text_changed
    if text_changed:
        if not ask_save_changes():
            return
    file = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file:
        with open(file, "r", encoding="utf-8") as f:
            content = f.read()
        text_area.delete(1.0, tk.END)
        text_area.insert(tk.END, content)
        current_file = file
        text_changed = False

def save_file():
    global current_file, text_changed
    if current_file:
        content = text_area.get(1.0, tk.END)
        with open(current_file, "w", encoding="utf-8") as f:
            f.write(content)
        text_changed = False
    else:
        save_as_file()

def save_as_file():
    global current_file, text_changed
    file = filedialog.asksaveasfilename(defaultextension=".txt",
                                        filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file:
        content = text_area.get(1.0, tk.END)
        with open(file, "w", encoding="utf-8") as f:
            f.write(content)
        current_file = file
        text_changed = False

def exit_app():
    if text_changed:
        if not ask_save_changes():
            return
    window.destroy()

def ask_save_changes():
    response = messagebox.askyesnocancel("Попередження", "Зберегти зміни перед виходом?")
    if response:  
        save_file()
        return True
    elif response is False: 
        return True
    else:  
        return False

def on_text_change(event):
    global text_changed
    text_changed = True

text_area.bind("<<Modified>>", on_text_change)

menu_bar = tk.Menu(window)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Відкрити", command=open_file)
file_menu.add_command(label="Зберегти", command=save_file)
file_menu.add_command(label="Зберегти як...", command=save_as_file)
file_menu.add_separator()
file_menu.add_command(label="Вийти", command=exit_app)
menu_bar.add_cascade(label="Файл", menu=file_menu)
window.config(menu=menu_bar)

window.protocol("WM_DELETE_WINDOW", exit_app)

window.mainloop()