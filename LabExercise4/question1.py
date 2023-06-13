#Tan Hyong Hsing
#20DDT21F1002

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Function to handle LOGIN button click event
def login():
    messagebox.showinfo("Welcome", "Welcome to Makan Makan Cafe")

# Function to handle CLICK HERE button click event
def display_name():
    name = name_entry.get()
    if name:
        name_label.config(text="Hello " + name)
    else:
        name_label.config(text="Hello <Empty>")

# Function to handle EXIT button click event
def exit_program():
    if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
        tan.destroy()

# Creating tkinter window
tan = tk.Tk()
tan.title('MAKAN MAKAN CAFE SYSTEM')
tan.geometry('500x300')

# label text for menu title
ttk.Label(tan, text="MAKAN MAKAN CAFE MENU",
          background='red', foreground="white",
          font=("Times New Roman", 15)).grid(row=0, column=1)

#select food label
ttk.Label(tan, text="Select the Food :",
          font=("Times New Roman", 10)).grid(column=0,
                                              row=5, padx=10, pady=10)

# Combobox creation
n = tk.StringVar()
food_choosen = ttk.Combobox(tan, width=27, textvariable=n)

# Adding combobox drop down list
food_choosen['values'] = ('Nasi Lemak',
                          'Satay',
                          'Roti Canai',
                          'Char Kway Teow',
                          'Laksa',
                          'Rendang',
                          'Hainanese Chicken Rice',
                          'Mee Goreng',
                          'Mihun Sup',
                          'Maggi Goreng')

food_choosen.grid(column=1, row=5)
food_choosen.current(0)  # Set default selection

# enter info label
instruction_label = ttk.Label(tan, text=" Please enter your info")
instruction_label.grid(column=1, row=6)

# Name entry
name_entry_label = ttk.Label(tan, text="Name:")
name_entry_label.grid(column=0, row=7, padx=10, pady=10, sticky='e')

name_entry = ttk.Entry(tan, width=30)
name_entry.grid(column=1, row=7, pady=10)

#password entry
password = ttk.Label(tan, text="Password:")
password.grid(column=0, row=8, padx=10, pady=10, sticky='e')

password = ttk.Entry(tan, width=30)
password.grid(column=1, row=8, pady=10)

# CLICK HERE button
click_here_button = ttk.Button(tan, text="CLICK HERE", command=display_name)
click_here_button.grid(row=10, column=1)

# Name output label
name_label = ttk.Label(tan, text="")
name_label.grid(column=2, row=11, columnspan=2, padx=10, pady=10)

# Login button
login_button = ttk.Button(tan, text="LOGIN", command=login)
login_button.grid(row=9, column=1)

# Exit button
exit_button = ttk.Button(tan, text="EXIT", command=exit_program)
exit_button.grid(row=11, column=1)

tan.mainloop()
