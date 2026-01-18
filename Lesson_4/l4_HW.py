import tkinter as tk
from tensorflow.keras.models import load_model
from PIL import Image, ImageDraw
import numpy as np
import matplotlib.pyplot as plt

Mdl = {
    "relu": load_model("Lesson 2/l2_mdl_relu.h5"),
    "sigmoid": load_model("Lesson 2/l2_mdl_sigmoid.h5"),
    "tanh": load_model("Lesson 2/l2_mdl_tanh.h5")
}

Current_Activation = "relu"

Gui = tk.Tk()
Gui.title("Drawing App")
colours = ["red", "blue", "green"]

canvas = tk.Canvas(Gui, width=400, height=400, bg="white")
canvas.pack()

Stored_Img = Image.new("L",(400,400),"white")
Made_Img = ImageDraw.Draw(Stored_Img) #Fixed, initialise image first

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
        width=8,
    )
    Made_Img.line([canvas.last_x,canvas.last_y,event.x,event.y], fill=255, width=8)
    canvas.last_x = event.x
    canvas.last_y = event.y

def set_red():
    canvas.current_colour = colours[0]

def set_blue():
    canvas.current_colour = colours[1]

def set_green():
    canvas.current_colour = colours[2]

def clear():
    global Stored_Img, Made_Img
    canvas.delete("all")
    Stored_Img = Image.new("L",(400,400),"white")
    Made_Img = ImageDraw.Draw(Stored_Img)

def set_relu():
    global Current_Activation
    Current_Activation = "relu"

def set_sigmoid():
    global Current_Activation
    Current_Activation = "sigmoid"

def set_tanh():
    global Current_Activation
    Current_Activation = "tanh"

def predict():
    bbox = Stored_Img.getbbox()
    if bbox:
        Img = Stored_Img.crop(bbox)
    else:
        Img = Stored_Img.copy()

    Img = Stored_Img.resize((28,28)).convert("L")
    Img = np.invert(np.array(Img))
    ImgArray = Img/255
    ImgArray = np.expand_dims(ImgArray, axis=0)

    Output = Mdl[Current_Activation].predict(ImgArray, verbose=0)
    print(Current_Activation, np.argmax(Output))

canvas.bind("<Button-1>", start_draw)
canvas.bind("<B1-Motion>", draw)

buttons = tk.Frame(Gui)
buttons.pack()

tk.Button(buttons, text="Red", bg="red", command=set_red).pack(side=tk.LEFT)
tk.Button(buttons, text="Blue", bg="blue", command=set_blue).pack(side=tk.LEFT)
tk.Button(buttons, text="Green", bg="green", command=set_green).pack(side=tk.LEFT)

tk.Button(buttons, text="ReLU", command=set_relu).pack(side=tk.LEFT)
tk.Button(buttons, text="Sigmoid", command=set_sigmoid).pack(side=tk.LEFT)
tk.Button(buttons, text="Tanh", command=set_tanh).pack(side=tk.LEFT)

tk.Button(buttons, text="Predict", command=predict).pack(side=tk.LEFT)
tk.Button(buttons, text="Clear", command=clear).pack(side=tk.LEFT)

Gui.mainloop()
