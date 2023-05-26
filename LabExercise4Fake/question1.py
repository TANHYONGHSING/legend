#Tan Hyong Hsing
#(20DDT21F1002)

import tkinter

def button_clicked():
    print()
    
lab4 = tkinter.Tk()
lab4.title("GUI Example_")
lab4.minsize(height=200 , width=200)


clickHere = tkinter.Button(text="Click Here" ,command=button_clicked)
clickHere.place(x=70,y=170)
lab4.mainloop()