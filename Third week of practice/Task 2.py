import tkinter as tk

window = tk.Tk()
window.geometry("500x300")
window.title("Друга програма")

label = tk.Label(window, text="", font=("Arial", 20))
label.pack(pady=20)

def say_hello():
    label.config(text="Вітаю, користувач!")

def clear_text():
    label.config(text="")

def exit_app():
    window.destroy()

btn_hello = tk.Button(window, text="Привітати", command=say_hello, font=("Arial", 14))
btn_hello.pack(pady=5)

btn_clear = tk.Button(window, text="Очистити", command=clear_text, font=("Arial", 14))
btn_clear.pack(pady=5)

btn_exit = tk.Button(window, text="Вийти", command=exit_app, font=("Arial", 14))
btn_exit.pack(pady=5)

window.mainloop()