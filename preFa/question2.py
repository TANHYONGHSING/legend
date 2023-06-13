import tkinter as tk

def add():
    result = float(value1.get()) + float(value2.get())
    result_label.config(text=f"Result: {result}")

def subtract():
    result = float(value1.get()) - float(value2.get())
    result_label.config(text=f"Result: {result}")

def multiply():
    result = float(value1.get()) * float(value2.get())
    result_label.config(text=f"Result: {result}")

def divide():
    result = float(value1.get()) / float(value2.get())
    result_label.config(text=f"Result: {result}")

def exit_program():
    root.destroy()

root = tk.Tk()
root.title("Calculator")

value1_label = tk.Label(root, text="Value 1:")
value1_label.grid(row=0, column=0, padx=10, pady=10)

value1 = tk.Entry(root)
value1.grid(row=0, column=1, padx=10, pady=10)

value2_label = tk.Label(root, text="Value 2:")
value2_label.grid(row=1, column=0, padx=10, pady=10)

value2 = tk.Entry(root)
value2.grid(row=1, column=1, padx=10, pady=10)

add_button = tk.Button(root, text="Add", command=add)
add_button.grid(row=2, column=0, padx=10, pady=10)

subtract_button = tk.Button(root, text="Subtract", command=subtract)
subtract_button.grid(row=2, column=1, padx=10, pady=10)

multiply_button = tk.Button(root, text="Multiply", command=multiply)
multiply_button.grid(row=3, column=0, padx=10, pady=10)

divide_button = tk.Button(root, text="Divide", command=divide)
divide_button.grid(row=3, column=1, padx=10, pady=10)

result_label = tk.Label(root, text="Result:")
result_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

exit_button = tk.Button(root, text="Exit", command=exit_program)
exit_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
