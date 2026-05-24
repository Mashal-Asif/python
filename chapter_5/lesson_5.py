# Exercise 1: Create an Interactive Line Plot GUI

import tkinter 
from tkinter import ttk
import sv_ttk
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,  
NavigationToolbar2Tk) 
import csv

root = tkinter.Tk()
sv_ttk.set_theme("dark")
root.title("Custom line plot")
root.geometry('500x800')

slope_slider = tkinter.Scale(root, from_=1, to=10, tickinterval=1, orient=tkinter.HORIZONTAL, length=400)
slope_slider.set(1)
slope_slider.pack()

fig = Figure(figsize = (8, 6), 
                 dpi = 100) 
canvas = FigureCanvasTkAgg(fig, master = root) 

def generate_plot(canvas, fig):
    if fig:
        fig.clear()
        
    m = slope_slider.get()
    x = np.linspace(0, 10, 100)
    y = m * x

    plot = fig.add_subplot(111)

    plot.plot(x, y)
    
    canvas.draw() 
    
    
plot_button = ttk.Button(root, text="Create Graph", command=lambda: generate_plot(canvas, fig))
plot_button.pack()

def download_csv():
    m = amplitude_slider.get()
    x = np.linspace(0, 10, 100)
    
    with open('slope.csv', 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['x', 'y'])
        writer.writeheader()
        for i in range(len(x)):
            y = m * x[i]
            writer.writerow({'x': x[i], 'y': y})

download_button = ttk.Button(root, text="Download Data", command=download_csv)
download_button.pack()

canvas.get_tk_widget().pack()

generate_plot(canvas, fig)

root.mainloop()