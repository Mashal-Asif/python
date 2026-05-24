# Exercise 1: Save Telemetry Logs

telemetry = [
    {
        "timestamp": "2024-03-30T07:58:27.999065",
        "temperature": 24.15,
        "pressure": 1082.28,
        "velocity": 2157.35,
        "altitude": 579.64,
        "power_level": 68.97,
        "orientation": {
            "roll": 63.34,
            "pitch": -174.83,
            "yaw": 220.57
        }
    },
    {
        "timestamp": "2024-03-30T07:47:56.999065",
        "temperature": -35.17,
        "pressure": 892.84,
        "velocity": 9366.16,
        "altitude": 821.66,
        "power_level": 25.56,
        "orientation": {
            "roll": -48.75,
            "pitch": -167.37,
            "yaw": 181.04
        }
    },
    {
        "timestamp": "2024-03-30T07:53:45.999065",
        "temperature": -5.28,
        "pressure": 1028.31,
        "velocity": 6538.57,
        "altitude": 729.16,
        "power_level": 88.36,
        "orientation": {
            "roll": 160.25,
            "pitch": 101.33,
            "yaw": 16.67
        }
    }
]

import csv
import json

with open('telemetry.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=telemetry[0].keys())
    writer.writeheader()
    writer.writerows(telemetry)
    
with open('telemetry.csv', 'r', newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
        
with open('telemetry.json', 'w') as file:
    json.dump(telemetry, file)
    
with open('telemetry.json', 'r') as file:
    data = json.load(file)

print(data)

# Exercise 2: Export data inside a tkinter application

rockets = [
    {
        'Name': 'Atlas V',
        'Operator': 'United Launch Alliance'
    },
    {
        'Name': 'Delta IV',
        'Operator': 'United Launch Alliance'
    }
]

import tkinter
from tkinter import ttk
import sv_ttk
import json

# Create a window
root = tkinter.Tk()

# Set the theme to dark mode!
sv_ttk.set_theme("dark")

def download_json():
    with open('rockets.json', 'w') as file:
        json.dump(rockets, file)
        
button = ttk.Button(root, text="Download JSON", command=download_json)
button.pack()

# Display the window
root.mainloop()