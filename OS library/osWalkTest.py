import os

path=r"C:\Users\HP\PycharmProjects\pythonProject.py\venv\Assignments"



for root,dir,file in os.walk(path):
    print("current root",root)
    # print( dir)
    print("current File",file)
