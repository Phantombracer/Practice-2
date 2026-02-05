import tkinter as tk
from tkinter import colorchooser, filedialog, messagebox

window = tk.Tk()
window.title("Графіка")
window.geometry("700x500")

current_color = "black"
draw_mode = "line"  
start_x = start_y = 0

canvas = tk.Canvas(window, width=600, height=400, bg="white")
canvas.pack(pady=20)

def choose_color():
    global current_color
    color = colorchooser.askcolor()[1]
    if color:
        current_color = color

def clear_canvas():
    canvas.delete("all")

def save_canvas():
    file = filedialog.asksaveasfilename(defaultextension=".ps",
                                        filetypes=[("PostScript files", "*.ps")])
    if file:
        try:
            canvas.postscript(file=file)
            messagebox.showinfo("Збережено", f"Зображення збережено у {file}")
        except Exception as e:
            messagebox.showerror("Помилка", str(e))

def set_line_mode():
    global draw_mode
    draw_mode = "line"

def set_circle_mode():
    global draw_mode
    draw_mode = "circle"

def on_button_press(event):
    global start_x, start_y
    start_x = event.x
    start_y = event.y
    if draw_mode == "circle":
        canvas.create_oval(start_x-5, start_y-5, start_x+5, start_y+5, fill=current_color, outline=current_color)

def on_drag(event):
    global start_x, start_y
    if draw_mode == "line":
        canvas.create_line(start_x, start_y, event.x, event.y, fill=current_color, width=2)
        start_x, start_y = event.x, event.y

canvas.bind("<Button-1>", on_button_press)
canvas.bind("<B1-Motion>", on_drag)

frame_buttons = tk.Frame(window)
frame_buttons.pack()

tk.Button(frame_buttons, text="Вибрати колір", command=choose_color).grid(row=0, column=0, padx=5)
tk.Button(frame_buttons, text="Лінія", command=set_line_mode).grid(row=0, column=1, padx=5)
tk.Button(frame_buttons, text="Коло", command=set_circle_mode).grid(row=0, column=2, padx=5)
tk.Button(frame_buttons, text="Очистити", command=clear_canvas).grid(row=0, column=3, padx=5)
tk.Button(frame_buttons, text="Зберегти", command=save_canvas).grid(row=0, column=4, padx=5)

window.mainloop()