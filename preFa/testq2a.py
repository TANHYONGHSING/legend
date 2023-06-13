# Tan Hyong Hsing (20DDT21F1002)

import tkinter as tk

tan = tk.Tk()
tan.title('Calculator')
tan.minsize(width=500 , height=500)

def add():
    result = float(value1_entry.get()) + float(value2_entry.get())
    result_label.config(text=f'Result : {result}')

def sub():
    result = float(value1_entry.get()) - float(value2_entry.get())
    result_label.config(text=f'Result : {result}')

def mul():
    result = float(value1_entry.get()) * float(value2_entry.get())
    result_label.config(text=f'Result : {result}')

def div():
    result = float(value1_entry.get()) / float(value2_entry.get())
    result_label.config(text=f'Result : {result}')

def exit():
    tan.destroy()

value1_label = tk.Label(text='Value 1 : ' , font=('fantasy' , 12 , 'bold'))
value1_label.grid(column=0 , row= 0 , padx= 10 , pady= 10)

value1_entry = tk.Entry(tan)
value1_entry.grid(column=1 , row=0 , padx=10 , pady=10)

value2_label = tk.Label(text='Value 2 : ' , font=('fantasy' ,12 , 'bold'))
value2_label.grid(column=0 ,row=1 , padx=10 , pady=10)

value2_entry = tk.Entry(tan)
value2_entry.grid(column= 1 , row=1 , padx=10 , pady=10)

result_label = tk.Label(text='Result : ' , font=('fantasy' , 12 , 'bold'))
result_label.grid(column=0 , row = 2 , padx= 10 , pady= 10)

add_button = tk.Button(text='Add' , command= add)
add_button.grid(column=0 , row= 3 , padx=10 , pady=10)

sub_button = tk.Button(text='Sub' , command= sub)
sub_button.grid(column=1 , row=3 , padx= 10 , pady= 10)

mul_button = tk.Button(text='mul' , command=mul)
mul_button.grid(column=0 , row=4 , padx= 10 , pady=10)

div_button = tk.Button(text='div' , command=div)
div_button.grid(column=1 , row=4 , padx= 10 , pady=10)

exit_button = tk.Button(text='exit' , command= exit)
exit_button.grid(column=2 , row= 5 , padx= 10 , pady= 10)

tan.mainloop()