#Tan Hyong Hsing
#(20DDT21F1002)

import tkinter

def button_clicked():
    print("I have been clicked")
    
lab4 = tkinter.Tk()
lab4.title("My First Python GUI program")
lab4.minsize(height=300 , width=300)


clickHere = tkinter.Button(text="Submit" ,command=button_clicked)
clickHere.place(x=130,y=0)
lab4.mainloop()