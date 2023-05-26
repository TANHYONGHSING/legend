#Tan Hyong Hsing
#(20DDT21F1002)

import tkinter

def button_clicked():
    weight = float(firstEntry.get())
    height = float(secondEntry.get())
    bmi = weight/(height**2)
    print(bmi)
    

tan = tkinter.Tk()
tan.title("Python GUI TUTORIALS")
tan.minsize(height=300 , width=500)

firstLabel = tkinter.Label(text="Enter base:",font=("Calibri",24,"bold"))
firstLabel.grid(column=0,row=0)

firstEntry = tkinter.Entry(bd=5)
firstEntry.grid(column=1,row=0)

secondLabel = tkinter.Label(text="Enter height:",font=("Calibri",24,"bold"))
secondLabel.grid(column=0,row=1)

secondEntry = tkinter.Entry(bd=5)
secondEntry.grid(column=1,row=1)

goButton = tkinter.Button(text="Go Click Me" ,command=button_clicked)
goButton.place(x=320 , y=30)

thirdLabel = tkinter.Label(text="Area of Triangle= 30.00",font=("Calibri",24,"bold"))
thirdLabel.place(x=70 , y=90)

tan.mainloop()