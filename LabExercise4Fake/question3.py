#Tan Hyong Hsing
#20DDT21F1002

import tkinter

lab4 = tkinter.Tk()
lab4.title("2 Number Addition")
lab4.minsize(height=340 , width=320)

def button_clicked():
    firstNum = int(firstEntry.get())
    secondNum = int(secondEntry.get())
    result = firstNum + secondNum
    thirdEntry.insert(0,result)

def clear():
    firstEntry.delete(0, tkinter.END)
    secondEntry.delete(0, tkinter.END)
    thirdEntry.delete(0, tkinter.END)


def close():
    lab4.quit()

labelframe = tkinter.LabelFrame(text="Number Addition",width=300 , height=300)
labelframe.place(x=10,y=0)

firstNum = tkinter.Label(text="First Number:",font=("Calibri",12))
firstNum.place(x=34 , y=30)

firstEntry = tkinter.Entry(bd=2)
firstEntry.place(x=130,y=35)

secondNum = tkinter.Label(text="Second Number:",font=("Calibri",12))
secondNum.place(x=15 , y=70)

secondEntry = tkinter.Entry(bd=2)
secondEntry.place(x=130,y=75)

result = tkinter.Label(text="Result:",font=("Calibri",12))
result.place(x=73 , y=110)

thirdEntry = tkinter.Entry(bd=2)
thirdEntry.place(x=130,y=115)

add = tkinter.Button(text="Add" ,command=button_clicked)
add.place(x=130,y=150)

clear = tkinter.Button(text="Clear" ,command=clear)
clear.place(x=200,y=150)

btnExit = tkinter.Button(text="Exit" ,command=close)
btnExit.place(x=260,y=310)

lab4.mainloop()