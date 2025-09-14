import tkinter as tk
from tkinter import filedialog
from pathlib import Path
import shutil
import os

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


target = tk.Entry(root, width=50)
target.insert(0,"")
target.pack()

dest = tk.Entry(root, width=50)
dest.insert(0,"")
dest.pack()


organize_button = tk.Button(root, text="Organize", command=openDir)
organize_button.pack()



# All file types
fileTypes = ["txt","7z","pdf","doc" , "docx", "xls", "xlsx", "ppt" , "pptx" , "odt" , "rtf",
             "jpg" , "jpeg" , "png", "gif", "bmp", "tiff", "svg", "webp", "ico", "mp3", "wav",
             "aac", "ogg", "m4a", "wma", "mp4", "avi", "mov", "wmv", "flv", "mkv", "webm", "3gp",
             "zip", "rar", "tar", "gz", "bz2", "iso", "py", "js", "html", "css", "java", "c", "cpp", "cs" ,"php", "rb", "go",
             "ts", "sh", "bat", "exe", "msi", "apk", "app", "bin", "com", "ini", "cfg", "json", "xml", "yaml", "env", "log",
             "ttf","otf", "woff","woff2", "db","sqlite","csv","md","epub","mobi"]


def process(directory):
    global current_dir

    # Target Directory
    targetDir = Path(directory)

    current_dir = os.listdir(targetDir)

    # Options for organizing by: 1) file type 2) name 3) date 


    # options = input("Option: ")
    return None


def organize(target, dest):   
    folder = os.path.join(current_dir, dest)
    os.makedirs(folder, exist_ok=True)

    count = 0
    for x in current_dir:
        s = x.split(".")
        if(len(s) > 1):
            if (s[-1] in fileTypes and s[-1] == target):
                print(s[-1])
                file = os.path.join(targetDir, x)
                shutil.move(file, folder)
        print(s[-1])
        count += 1
        if count == 5: break

    return None


root.mainloop()

