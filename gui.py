import tkinter as tk
import os

root = tk.Tk()

root.title("File Organizer")
root.geometry("400x300")

button = tk.Button(root, text="Button", command=print("hello"))

dropdown = tk.OptionMenu(root, tk.StringVar(), "Option 1", "Option 2")

button.pack()
dropdown.pack()
root.mainloop()