import os
from pathlib import Path
import shutil

# Target Directory
TARGET_DIRECTORY = Path("C://Users/Alyx/Downloads")

dir_list = os.listdir(TARGET_DIRECTORY)

# All file types
fileTypes = ["txt","7z","pdf","doc" , "docx", "xls", "xlsx", "ppt" , "pptx" , "odt" , "rtf",
             "jpg" , "jpeg" , "png", "gif", "bmp", "tiff", "svg", "webp", "ico", "mp3", "wav",
             "aac", "ogg", "m4a", "wma", "mp4", "avi", "mov", "wmv", "flv", "mkv", "webm", "3gp",
             "zip", "rar", "tar", "gz", "bz2", "iso", "py", "js", "html", "css", "java", "c", "cpp", "cs" ,"php", "rb", "go",
             "ts", "sh", "bat", "exe", "msi", "apk", "app", "bin", "com", "ini", "cfg", "json", "xml", "yaml", "env", "log",
             "ttf","otf", "woff","woff2", "db","sqlite","csv","md","epub","mobi"]
# Options for organizing by: 1) file type 2) name 3) date 


# options = input("Option: ")
target = input("File Type: ")
dest = input("Folder Name: ")
folder = os.path.join(TARGET_DIRECTORY, dest)
os.makedirs(folder, exist_ok=True)

count = 0
for x in dir_list:
    s = x.split(".")
    if(len(s) > 1):
        if (s[-1] in fileTypes and s[-1] == target):
            print(s[-1])
            file = os.path.join(TARGET_DIRECTORY, x)
            shutil.move(file, folder)
    print(s[-1])
    count += 1
    if count == 5: break




