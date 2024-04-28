# Author: OM
import os

# Checking file
file_path=r"C:\Users\HP\PycharmProjects\pythonProject.py\venv\Assignments\analysis_project\append_to_sql.py"

if os.path.exists(file_path):
    print("File Exists")
else:
    print("not Exists")


# Checking Directory
dirpath=r"C:\Users\HP\PycharmProjects\pythonProject.py\venv\Assignments\analysis_project\daily_files"

if os.path.isdir(dirpath):
    print("Directory Exists")
else:
    print("Directory not Exists")


# Gives file Name
path = r"C:\Users\HP\PycharmProjects\pythonProject.py\venv\Assignments\analysis_project"
print(os.path.basename(path))


# Gives root path and extension
path = r"C:\Users\HP\PycharmProjects\pythonProject.py\venv\Assignments\analysis_project\append_to_sql.py"
root, ext = os.path.splitext(path)
print("Root:", root)
print("Extension:", ext)