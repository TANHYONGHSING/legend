#Tan Hyong Hsing
#(20DDT21F1002)

import tkinter

def button_clicked():
    print("bmi")

tan = tkinter.Tk()
tan.title("My first GUI")
tan.minsize(height=300 , width=300)
'''
my_label = tkinter.Label(text="I Am A Label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
my_label.grid(column=0, row=0)
'''
label= tkinter.Label(text="Label")
label.grid(column=0,row=0) 
'''
button = tkinter.Button(text="Go Click Me" ,command=button_clicked)
button.grid(column=1, row=1)
'''
button = tkinter.Button(text="Button")
button.grid(column=1,row=1)

new_button = tkinter.Button(text="New Button")
new_button.grid(column=2,row=0)

input = tkinter.Entry(width=10)
print(input.get())
input.grid(column=3, row=2)
'''
my_button = tkinter.Button(text="Click Me")
my_button.grid(column=1,row=1)

input = tkinter.Entry(width=10)
print(input.get())
input.grid(column=2, row=2)
'''

tan.mainloop()