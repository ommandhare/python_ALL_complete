"""
Develop a report showing total data size, by evey directory in a given location.

"""
import os

root_dir = r"C:\Users\HP\PycharmProjects\pythonProject.py\venv\Assignments"



for files,dir,subdir in os.walk(root_dir):
    print(files)

total_size = 0

    # Walk through each directory and file in the given directory
for root, dirs, files in os.walk(root_dir):
    # Add the size of each file to the total size
    for file in files:
        file_path = os.path.join(root, file)
        total_size += os.path.getsize(file_path)

print(total_size)

report = {}

# Walk through each directory in the root directory
for root, dirs, files in os.walk(root_dir):
    # Calculate the total size of files in the current directory
    report[root] = total_size

print(report)
