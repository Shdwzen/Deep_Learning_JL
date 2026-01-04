import tkinter as tk

Gui = tk.Tk()
Gui.title("Drawing App")
colours = ["red", "blue", "green"]

canvas = tk.Canvas(Gui, width=400, height=400, bg="white")
canvas.pack()

canvas.current_colour = colours[0]
canvas.last_x = 0
canvas.last_y = 0

def start_draw(event):
    canvas.last_x = event.x
    canvas.last_y = event.y

def draw(event):
    canvas.create_line(
        canvas.last_x, canvas.last_y,
        event.x, event.y,
        fill=canvas.current_colour,
        width=2
    )
    canvas.last_x = event.x
    canvas.last_y = event.y

def set_red():
    canvas.current_colour = colours[0]

def set_blue():
    canvas.current_colour = colours[1]

def set_green():
    canvas.current_colour = colours[2]

def clear():
    canvas.delete("all")

canvas.bind("<Button-1>", start_draw)
canvas.bind("<B1-Motion>", draw)

buttons = tk.Frame(Gui)
buttons.pack()

tk.Button(buttons, text="Red", bg="red", command=set_red).pack(side=tk.LEFT)
tk.Button(buttons, text="Blue", bg="blue", command=set_blue).pack(side=tk.LEFT)
tk.Button(buttons, text="Green", bg="green", command=set_green).pack(side=tk.LEFT)
tk.Button(buttons, text="Clear", command=clear).pack(side=tk.LEFT)

Gui.mainloop()
