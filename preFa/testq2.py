# THH (20DDT21F1002)

import tkinter as tk

tan = tk.Tk()
tan.title('Calculator')
tan.minsize(width=500 , height=500)

def add ():
    result = float(entry1.get()) + float(entry2.get())
    result_lbl.config(text=f'Result : {result}')

def exit():
    tan.destroy()

label1 = tk.Label(text='Value 1 :' , font=('fantasy' , 12 , 'bold'))
label1.grid(column=0 , row= 0)

# Create a LabelFrame
frame = tk.LabelFrame(tan, text="Calculator")
frame.pack(padx=10, pady=10)

entry1 = tk.Entry(tan)
entry1.grid(column=1 , row=0)

label2 = tk.Label(text='Value 2 :' , font=('fantasy' , 12 , 'bold'))
label2.grid(column=0 , row= 1)

entry2 = tk.Entry(tan)
entry2.grid(column=1 , row=1)

add_btn = tk.Button(text='add' , command=add)
add_btn.grid(column=0 , row=2)

result_lbl = tk.Label(text='Result : ' , font=('fantasy',12 ,'bold'))
result_lbl.grid(column=0 , row=3)

exitbtn = tk.Button(text='exit' , command=exit)
exitbtn.grid(column=2 , row= 3)

tan.mainloop()