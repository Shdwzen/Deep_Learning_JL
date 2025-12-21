import tkinter as tk

Screen = tk.Tk()
Screen.title("Cool")
Screen.geometry("10x60")

def smth():
    print("Helo!!!")

Bttn1 = tk.Button(Screen,text="Hi",bg="Blue",fg="Red",borderwidth=5,activebackground="Red",relief="ridge",font=("Comic Sans",18,"bold"),command=smth)

Bttn1.place(x=0,y=0)







Screen.mainloop()