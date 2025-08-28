import os
from pathlib import Path
import shutil

# Target Directory
TARGET_DIRECTORY = Path("C://Users/Alyx/Downloads")

dir_list = os.listdir(TARGET_DIRECTORY)

# Options for organizing by: 1) file type 2) name 3) date 


# options = input("Option: ")

# if(options == 1):
count = 0
for x in dir_list:
    s = x.split(".")
    print(s[0])
    print("file type---")
    if(len(s) > 1):
        print(s[1])
    count += 1
    if count == 5: break




