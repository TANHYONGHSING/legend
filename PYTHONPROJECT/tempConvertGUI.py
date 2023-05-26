#Tan Hyong Hsing
#(20DDT21F1002)

import tkinter

def button_clicked():
    celsius = float(celsiusEntry.get())
    fahrenheit = (celsius * 9/5) + 32
    kelvin = celsius + 273.15
    answerLabel["text"] = "The temperature in fahrenheit is " +str(fahrenheit) +" °F"
    answerLabel2["text"] = "The temperature in kelvin is " +str(kelvin)+" K"
    

screen = tkinter.Tk()
screen.title("Temperature Converter")
screen.minsize(height=200 , width=500)

celsiuslbl = tkinter.Label(text="Give me the temperature in °C",font=("Fantasy",24,"bold"))
celsiuslbl.pack()

celsiusEntry = tkinter.Entry(bd=5)
celsiusEntry.pack()

checkBtn = tkinter.Button(text="Convert Temperature" ,command=button_clicked)
checkBtn.pack()

answerLabel = tkinter.Label(text="", font=("Fantasy",12,"bold"))
answerLabel.pack()

answerLabel2 = tkinter.Label(text="", font=("Fantasy",12,"bold"))
answerLabel2.pack()

screen.mainloop()