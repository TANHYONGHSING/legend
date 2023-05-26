#Tan Hyong Hsing
#(20DDT21F1002)

import tkinter

def button_clicked():
    weight = float(firstEntry.get())
    height = float(secondEntry.get())
    bmi = weight/(height**2)
    print(bmi)
    

tan = tkinter.Tk()
tan.title("My first GUI")
tan.minsize(height=500 , width=500)

firstLabel = tkinter.Label(text="Set The Height",font=("Calibri",24,"bold"))
firstLabel.place(x=0, y=70)

secondEntry = tkinter.Entry(bd=5)
firstLabel.place(x=50, y=60)

secondLabel = tkinter.Label(text="Set The Weight",font=("Calibri",24,"bold"))
secondLabel.place(x=10, y=100)

firstEntry = tkinter.Entry(bd=5)
firstEntry.place(x=50, y=90)

goButton = tkinter.Button(text="Go Click Me" ,command=button_clicked)
goButton.place(x=30, y=110)
tan.mainloop()