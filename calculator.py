import tkinter as tk
from tkinter import messagebox
import math

# Function to update display
def click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(value))

# Function to clear display
def clear():
    entry.delete(0, tk.END)

# Function to calculate result
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except ZeroDivisionError:
        messagebox.showerror("Error", "Division by zero is not allowed")
        clear()
    except:
        messagebox.showerror("Error", "Invalid Input")
        clear()

# Square root function
def square_root():
    try:
        result = math.sqrt(float(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        messagebox.showerror("Error", "Invalid Input")

# Percentage function
def percentage():
    try:
        result = float(entry.get()) / 100
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        messagebox.showerror("Error", "Invalid Input")

# Main window
root = tk.Tk()
root.title("Basic Calculator")
root.geometry("350x450")
root.resizable(False, False)

# Entry widget
entry = tk.Entry(root, font=("Arial", 20), bd=10, relief=tk.RIDGE, justify="right")
entry.grid(row=0, column=0, columnspan=4, pady=10)

# Button layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

# Create buttons
for (text, row, col) in buttons:
    if text == '=':
        btn = tk.Button(root, text=text, width=8, height=3,
                        command=calculate)
    else:
        btn = tk.Button(root, text=text, width=8, height=3,
                        command=lambda t=text: click(t))

    btn.grid(row=row, column=col, padx=5, pady=5)

# Extra buttons
tk.Button(root, text="C", width=8, height=3,
          command=clear).grid(row=5, column=0, pady=5)

tk.Button(root, text="√", width=8, height=3,
          command=square_root).grid(row=5, column=1, pady=5)

tk.Button(root, text="%", width=8, height=3,
          command=percentage).grid(row=5, column=2, pady=5)

# Keyboard support
root.bind("<Return>", lambda event: calculate())

# Run application
root.mainloop()