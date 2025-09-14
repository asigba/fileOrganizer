import tkinter as tk
from tkinter import filedialog
from main import process

root = tk.Tk()

root.title("File Organizer")
root.geometry("400x300")

current_dir = ""

def openDir():
    global current_dir


    dir = filedialog.askdirectory()
    # process(dir)
    current_dir = dir
    entry.delete(0, tk.END)
    entry.insert(0, current_dir)
    return dir

entry = tk.Entry(root, width=50)
entry.insert(0,current_dir)
entry.pack()

select_folder_button = tk.Button(root, text="Select Folder", command=openDir)
select_folder_button.pack()

organize_button = tk.Button(root, text="Organize", command=openDir)
organize_button.pack()

root.mainloop()

