import tkinter as tk

window = tk.Tk()
window.geometry("1024x768")       
window.title("Перша програма")    

label = tk.Label(window, text="Hello, world!", font=("Arial", 24))
label.pack(pady=50) 

button = tk.Button(window, text="Закрити", command=window.destroy, font=("Arial", 14))
button.pack()

window.mainloop()