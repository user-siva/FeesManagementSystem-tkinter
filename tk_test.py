import tkinter as tk
from tkinter import tix
import ttkbootstrap

# Create the main window
root = tk.Tk()

# Create a button with a shadow effect
button = ttkbootstrap.Button(root, text="Click me!",
                             style=ttkbootstrap.STYLE_CLASS['shadow'])
button.pack()

# Run the tkinter event loop
root.mainloop()
