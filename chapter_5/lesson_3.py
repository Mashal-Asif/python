# Exercise 1: Basic Components with Sun Valley

import tkinter
from tkinter import ttk
import sv_ttk

# Create a window
root = tkinter.Tk()

# Add a Label component
text = ttk.Label(root, text = "Hello World")
text.pack()

# Add a Button component
button = ttk.Button(root, text="Click Button")
button.pack()

# Set the theme to dark mode!
sv_ttk.set_theme("dark")

root.mainloop()

# Exercise 2: Rocketship Form with Sun Valley

# Create a window
root = tkinter.Tk()
root.title("Rocketship Form")
root.geometry('500x300')

# Set the theme to dark mode!
sv_ttk.set_theme("dark")

# Create a Style instance to make custom styles!
style = ttk.Style()

# Configure a class name called Padding.TLabel" which shows a top padding of 10px and a bottom padding of 5px when applied
style.configure('Padding.TLabel', padding=(0, 10, 0, 5))  # (left, top, right, bottom)

# Create Name Label
name_label = ttk.Label(root, text="Rocketship Name:", style='Padding.TLabel')
name_label.pack()

# Create Input for First Name
name_entry = ttk.Entry(root)
name_entry.pack()

# Create Destination Label
destination_label = ttk.Label(root, text="Rocketship Destination:", style='Padding.TLabel')
destination_label.pack()

# Create Input for Destination
destination_entry = ttk.Entry(root)
destination_entry.pack()

# Create Mass Label
mass_label = ttk.Label(root, text="Rocketship Mass:", style='Padding.TLabel')
mass_label.pack()

# Create Input for Mass
mass_entry = ttk.Entry(root)
mass_entry.pack()

# Create a Label for Result Output
result_label = ttk.Label(root, text="Output: ", style='Padding.TLabel')
result_label.pack()


def blast_off():
    # Extract input from the fields 
    name = name_entry.get()
    destination = destination_entry.get()
    mass = mass_entry.get()

    output = f"{name} is heading to the {destination} and weighs {mass} kg!" 
    result_label.configure(text=output)

register_button = ttk.Button(root, text="Blast Off", command=blast_off)
register_button.pack()

root.mainloop()