import math
import tkinter as tk
from tkinter import *

Window = Tk()
Window.title("Calculator")
Window.geometry("500x445")

# For the Black Background
Window.configure(background="#17161b")

Equation=""

# When i prees a symbol or number to show on screen
def showing(value):
    global Equation
    Equation+=value
    Results.config(text=Equation)

# When i press Button "C" the Tab will empty
def clear():
    global Equation
    Equation =""
    Results.config(text=Equation)

# To calculate the results
def Calculation():
    global Equation
    Result =""
    if Equation != "":
        try:
            Result= eval(Equation)
        except:
            Result = "Try again"
            Equation = ""
    Results.config(text=Result)

# Results Box
Results = Label(Window, width= 25, height=1, text="", font=("arial",30))
Results.pack()

#Adding Buttons
Button(Window,text="C", width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#282828",bg="#228B22",command=lambda: clear()).place(x=1,y= 50)
Button(Window,text="/", width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#282828",bg="#808A87",command=lambda: showing("/")).place(x=125,y= 50)
Button(Window,text="%", width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#282828",bg="#808A87",command=lambda: showing("%")).place(x=250,y= 50)
Button(Window,text="*", width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#282828",bg="#808A87",command=lambda: showing("*")).place(x=375,y= 50)

Button(Window,text="7", width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#282828",bg="#27408B",command=lambda:showing("7")).place(x=1,y= 125)
Button(Window,text="8", width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#282828",bg="#27408B",command=lambda:showing("8")).place(x=125,y= 125)
Button(Window,text="9", width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#282828",bg="#27408B",command=lambda:showing("9")).place(x=250,y= 125)
Button(Window,text="-", width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#282828",bg="#808A87",command=lambda:showing("-")).place(x=375,y= 125)

Button(Window,text="4", width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#282828",bg="#27408B",command=lambda:showing("4")).place(x=1,y= 205)
Button(Window,text="5", width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#282828",bg="#27408B",command=lambda:showing("5")).place(x=125,y= 205)
Button(Window,text="6", width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#282828",bg="#27408B",command=lambda:showing("6")).place(x=250,y= 205)
Button(Window,text="+", width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#282828",bg="#808A87",command=lambda:showing("+")).place(x=375,y= 205)

Button(Window,text="1", width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#282828",bg="#27408B",command=lambda:showing("1")).place(x=1,y= 285)
Button(Window,text="2", width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#282828",bg="#27408B",command=lambda:showing("2")).place(x=125,y= 285)
Button(Window,text="3", width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#282828",bg="#27408B",command=lambda:showing("3")).place(x=250,y= 285)
Button(Window,text="=", width=5, height=3, font=("arial",30,"bold"), bd=1,fg="#282828",bg="#808A87",command=lambda:Calculation()).place(x=375,y= 285)

Button(Window,text=".", width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#282828",bg="#27408B",command=lambda:showing(".")).place(x=246,y= 365)
Button(Window,text="0", width=10, height=1, font=("arial",30,"bold"), bd=1,fg="#282828",bg="#27408B",command=lambda:showing("0")).place(x=1,y= 365)

Window.mainloop()