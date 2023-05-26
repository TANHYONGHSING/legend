#Tan Hyong Hsing
#(20DDT21F1002)

import tkinter

def button_clicked():
    weight = float(firstEntry.get())
    height = float(secondEntry.get())
    bmi = weight/(height**2)
    print(bmi)
    

tan = tkinter.Tk()
tan.title("Calculator")
tan.minsize(height=250 , width=400)

Label = tkinter.Label(text="Quadratic Equation Solver",font=("Calibri",20,"bold"))
Label.place(x=70,y=0)

firstLabel = tkinter.Label(text="A Value:",font=("Calibri",20,"bold"))
firstLabel.place(x=30,y=50)

firstEntry = tkinter.Entry(bd=5)
firstEntry.place(x=160,y=60)

secondLabel = tkinter.Label(text="B Value:",font=("Calibri",20,"bold"))
secondLabel.place(x=30,y=80)

secondEntry = tkinter.Entry(bd=5)
secondEntry.place(x=160,y=90)

thirdLabel = tkinter.Label(text="C Value:",font=("Calibri",20,"bold"))
thirdLabel.place(x=30 , y=110)

thirdEntry = tkinter.Entry(bd=5)
thirdEntry.place(x=160,y=120)

soButton = tkinter.Button(text="Solve" ,command=button_clicked)
soButton.place(x=170 , y=150)

clButton = tkinter.Button(text="Clear" ,command=button_clicked)
clButton.place(x=270 , y=150)

fourthLabel = tkinter.Label(text="Solution: x=5.70,x=-0.70",font=("Calibri",24,"bold"))
fourthLabel.place(x=0 , y=180)

tan.mainloop()