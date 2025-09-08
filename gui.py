import tkinter as tk

root = tk.Tk()

root.title("File Organizer")
root.geometry("400x300")

button = tk.Button(root, text="Button", command=print("hello"))
button.pack()
root.mainloop()