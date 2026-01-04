import tkinter as tk
from tensorflow.keras.models import load_model
from PIL import Image, ImageDraw
import numpy as np
import matplotlib.pyplot as plt

Mdl = load_model("Lesson 2/l2_mdl1.h5")

Gui = tk.Tk()
Gui.title("Drawing App")
colours = ["red", "blue", "green"]

canvas = tk.Canvas(Gui, width=400, height=400, bg="white")
canvas.pack()
Stored_Img = Image.new("L",(400,400),"white")
Made_Img = ImageDraw.Draw(Stored_Img)

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
        width=2,
    )
    canvas.last_x = event.x
    canvas.last_y = event.y
    Made_Img.line([canvas.last_x,canvas.last_y,event.x,event.y])

def set_red():
    canvas.current_colour = colours[0]

def set_blue():
    canvas.current_colour = colours[1]

def set_green():
    canvas.current_colour = colours[2]

def clear():
    global Stored_Img
    canvas.delete("all")
    Stored_Img = Image.new("L",(400,400),"white")
    Made_Img = ImageDraw.Draw(Stored_Img)

def predict():
    global Stored_Img
    Stored_Img = Stored_Img.resize((28,28)).convert("L")
    ImgArray = np.array(Stored_Img)
    ImgArray = ImgArray/255
    ImgArray = np.expand_dims(ImgArray, axis=0)
    Output = Mdl.predict(ImgArray)
    print(np.argmax(Output))
    


canvas.bind("<Button-1>", start_draw)
canvas.bind("<B1-Motion>", draw)

buttons = tk.Frame(Gui)
buttons.pack()

tk.Button(buttons, text="Red", bg="red", command=set_red).pack(side=tk.LEFT)
tk.Button(buttons, text="Blue", bg="blue", command=set_blue).pack(side=tk.LEFT)
tk.Button(buttons, text="Green", bg="green", command=set_green).pack(side=tk.LEFT)
tk.Button(buttons, text="Predict", command=predict).pack(side=tk.LEFT)
tk.Button(buttons, text="Clear", command=clear).pack(side=tk.LEFT)



Gui.mainloop()