# Exercise 1: Create your own Tkinter Display

import tkinter as tk
window = tk.Tk()
label = tk.Label(text="My First Display")
label.pack()
window.mainloop()

# Exercise 2: Create an Addition Calculator

window = tk.Tk()
window.title("Addition Calculator")

# Add label for the calculator title
title_label = tk.Label(window, text="Addition Calculator")
title_label.pack(pady=10)

# Create the main form contents 
number1_label = tk.Label(window, text="Number 1:")
number1_label.pack()
number1_entry = tk.Entry(window)
number1_entry.pack(pady=5)

number2_label = tk.Label(window, text="Number 2:")
number2_label.pack()
number2_entry = tk.Entry(window)
number2_entry.pack(pady=5)

# Define the addition function
def add_numbers():
    result = int(number1_entry.get()) + int(number2_entry.get())
    result_label.config(text=f"Sum: {result}")
    
# Add button to perform addition
add_button = tk.Button(window, text="Add", command=add_numbers)
add_button.pack(pady=10)

# Add label to display result
result_label = tk.Label(window, text="")
result_label.pack()

# Display the window
window.mainloop()