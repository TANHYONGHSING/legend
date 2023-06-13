#TAN HYONG HSING (20DDT21F1002)

import tkinter as tk

def combine():
    suggestion = str(first_name_entry.get()) + str(second_name_entry.get()) + '@gmail.com'
    suggestionentry.config(f'{suggestion}')

def clear():
    suggestionlbl.delete()
    first_name_entry.delete()
    second_name_entry.delete()

def exit():
    tan.destroy()

tan = tk.Tk()
tan.title('Automatic Username')
tan.minsize(width=500, height=500)

tan_frame = tk.LabelFrame(text='Username Suggestion')
tan_frame.grid(column=0 , row=0 , padx=10 , pady=10)

first_namelbl = tk.Label(tan,text='      First Name : ' , font=('fantasy' , 12 , 'bold'))
first_namelbl.grid(column=0 , row=0 , padx= 10 , pady= 10)

first_name_entry = tk.Entry(tan)
first_name_entry.grid(column=1 , row=0 ,padx= 10 ,pady= 10)

second_namelbl = tk.Label(tan,text='Second Name : ' , font=('fantasy' , 12 , 'bold'))
second_namelbl.grid(column=0 , row=1 , padx= 10 , pady= 10)

second_name_entry = tk.Entry(tan)
second_name_entry.grid(column=1 , row=1 ,padx= 10 ,pady= 10)

suggestionlbl = tk.Label(tan,text='      Suggested : ' , font=('fantasy' , 12 , 'bold'))
suggestionlbl.grid(column=0 , row= 2 , padx=10 , pady= 10)

suggestionentry = tk.Entry(tan)
suggestionentry.grid(column=1 , row= 2 , padx=10 , pady= 10)
                   
combine_btn = tk.Button(tan,text='Combine' , command=combine)
combine_btn.grid(column=1 , row= 3 )

clear_btn = tk.Button(tan,text='Clear' , command=clear)
clear_btn.grid(column=2,row= 3 )

exitbtn = tk.Button(text='Exit' , command=exit)
exitbtn.grid(column=3 , row= 4 ,padx=10 , pady= 10)



tan.mainloop()