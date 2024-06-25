import math
import tkinter as tk
from tkinter import *

Window = Tk()
Window.title("Calculator")
Window.geometry("524x539")


Window.configure(background="#17161b")

Results = Label(Window, width= 30, height=3, text="", font=("arial",30))
Results.pack()

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

# To calculate the square of the number ( x² )
def square():
    global Equation
    if Equation != "":
        try:
            value = str(eval(Equation)**2)
            Equation = value
            Results.config(text=Equation)
        except:
            Results.config(text="Try again")
            Equation = ""

# To calculate the power of the number ( xᵡ )
def power_up():
    global Equation
    Equation += "**"
    Results.config(text=Equation)

# To calculate the inverse of division ( 1/x )
def inverse ():
    global Equation 
    if Equation != "":
        try:
            value = str( 1/eval(Equation))
            Equation = value
            Results.config(text=Equation)
        except:
            Results.config(text="Try again")
            Equation = ""

# To calculate the root of the number ( √x )
def root():
    global Equation
    if Equation != "":
        try:
            value = str(eval(Equation)**0.5)
            Equation = value
            Results.config(text=Equation)
        except:
            Results.config(text="Try again")
            Equation = ""

# To calculate the factorial of the number ( x! )
def factorial():
    global Equation
    if Equation != "":
        try:
            value = str(math.factorial(int(eval(Equation))))
            Equation = value
            Results.config(text=Equation)
        except:
            Results.config(text="Try again")
            Equation = ""


# Creating Buttons 

Button(Window,text="C", width=4, height=1, font=("arial",30,"bold"), bd=1,fg="#282828",bg="#228B22",command=lambda: clear()).place(x=1,y= 140) 
Button(Window,text="x²", width=4, height=1, font=("arial",30,"bold"), bd=1,fg="#282828",bg="#808A87",command=lambda: square()).place(x=105,y= 140)
Button(Window,text="xᵡ", width=4, height=1, font=("arial",30,"bold"), bd=1,fg="#282828",bg="#808A87",command=lambda: power_up()).place(x=210,y= 140)
Button(Window,text="*", width=4, height=1, font=("arial",30,"bold"), bd=1,fg="#282828",bg="#808A87",command=lambda: showing("*")).place(x=315,y= 140)
Button(Window,text="/", width=4, height=1, font=("arial",30,"bold"), bd=1,fg="#282828",bg="#808A87",command=lambda: showing("/")).place(x=420,y= 140)

Button(Window,text="7", width=4, height=1, font=("arial",30,"bold"), bd=1,fg="#282828",bg="#27408B",command=lambda:showing("7")).place(x=105,y= 220)
Button(Window,text="8", width=4, height=1, font=("arial",30,"bold"), bd=1,fg="#282828",bg="#27408B",command=lambda:showing("8")).place(x=210,y= 220)
Button(Window,text="9", width=4, height=1, font=("arial",30,"bold"), bd=1,fg="#282828",bg="#27408B",command=lambda:showing("9")).place(x=315,y= 220)
Button(Window,text="-", width=4, height=1, font=("arial",30,"bold"), bd=1,fg="#282828",bg="#808A87",command=lambda:showing("-")).place(x=420,y= 220)

Button(Window,text="4", width=4, height=1, font=("arial",30,"bold"), bd=1,fg="#282828",bg="#27408B",command=lambda:showing("4")).place(x=105,y= 300)
Button(Window,text="5", width=4, height=1, font=("arial",30,"bold"), bd=1,fg="#282828",bg="#27408B",command=lambda:showing("5")).place(x=210,y= 300)
Button(Window,text="6", width=4, height=1, font=("arial",30,"bold"), bd=1,fg="#282828",bg="#27408B",command=lambda:showing("6")).place(x=315,y= 300)
Button(Window,text="+", width=4, height=1, font=("arial",30,"bold"), bd=1,fg="#282828",bg="#808A87",command=lambda:showing("+")).place(x=420,y= 300)

Button(Window,text="1", width=4, height=1, font=("arial",30,"bold"), bd=1,fg="#282828",bg="#27408B",command=lambda:showing("1")).place(x=105,y= 380)
Button(Window,text="2", width=4, height=1, font=("arial",30,"bold"), bd=1,fg="#282828",bg="#27408B",command=lambda:showing("2")).place(x=210,y= 380)
Button(Window,text="3", width=4, height=1, font=("arial",30,"bold"), bd=1,fg="#282828",bg="#27408B",command=lambda:showing("3")).place(x=315,y= 380)
Button(Window,text="=", width=4, height=3, font=("arial",30,"bold"), bd=1,fg="#282828",bg="#808A87",command=lambda:Calculation()).place(x=420,y= 380)

Button(Window,text=".", width=4, height=1, font=("arial",30,"bold"), bd=1,fg="#282828",bg="#27408B",command=lambda:showing(".")).place(x=315,y= 460)
Button(Window,text="0", width=8, height=1, font=("arial",30,"bold"), bd=1,fg="#282828",bg="#27408B",command=lambda:showing("0")).place(x=114,y= 460)

Button(Window,text="1/x", width=4, height=1, font=("arial",30,"bold"), bd=1,fg="#282828",bg="#808A87",command=lambda: inverse()).place(x=1,y= 220)
Button(Window,text="(", width=3, height=1, font=("arial",30,"bold"), bd=1,fg="#282828",bg="#808A87",command=lambda: showing("(")).place(x=1,y= 460)
Button(Window,text=")", width=2, height=1, font=("arial",30,"bold"), bd=1,fg="#282828",bg="#808A87",command=lambda: showing(")")).place(x=65,y= 460)
Button(Window,text="√x", width=4, height=1, font=("arial",30,"bold"), bd=1,fg="#282828",bg="#808A87",command=lambda: root()).place(x=1,y= 300)
Button(Window,text="x!", width=4, height=1, font=("arial",30,"bold"), bd=1,fg="#282828",bg="#808A87",command=lambda: factorial()).place(x=1,y= 380)
Window.mainloop()