from tkinter import *
def sel():
   selection = "Value = " + str(var.get())
   label.config(text = selection)
   fahrenheit = (var.get()* 9/5) + 32
   answerLabel["text"] = "Fahrenheit is " +str(fahrenheit) +" °F"
 
root = Tk()
 


var = DoubleVar()
scale = Scale( root, variable = var )
scale.pack(anchor=CENTER)
 
button = Button(root, text="Get Scale Value", command=sel)
button.pack(anchor=CENTER)
 
label = Label(root)
label.pack()
 
answerLabel = Label(text="", font=("Fantasy",12))
answerLabel.pack()

root.mainloop()