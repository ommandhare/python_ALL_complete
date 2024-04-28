"""
Walk path given by users (os.walk) and generate report about number of files, no of directories and size of every directory

"""

import os

report = {}
root_dir = input("Enter the root directory path: ")

if not os.path.exists(root_dir):
    print("The specified directory does not exist.")

print("\nDirectory Report:")

cnt=0
for root, dirs, files in os.walk(root_dir):
        num_files = len(files)
        num_dirs = len(dirs)
        dir_size = sum(os.path.getsize(os.path.join(root, filename)) for filename in files)
        print(f"\nDirectory:",cnt)
        print("Number of files: ", num_files)
        print("Number of directories: ", num_dirs)
        print("Total size:", dir_size)
        cnt+=1






