"""
Write a program to move files from one directory to another (archive files)

"""

import os
import shutil


source_dir =  r"C:\Users\HP\PycharmProjects\pythonProject.py\venv\Assignments\OS library"
destination_dir =r"C:\Users\HP\PycharmProjects\pythonProject.py\venv\Assignments\testcopyfolder"

files_to_move = os.listdir(source_dir)

print(files_to_move)

for file_name in files_to_move:
    source_path = os.path.join(source_dir, file_name)
    destination_path = os.path.join(destination_dir, file_name)
    shutil.copy(source_path, destination_path)
    # shutil.move(source_path, destination_path)
print("All files moved successfully.")
