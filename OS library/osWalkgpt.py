import os

def get_directory_size(directory):
    total_size = 0
    for dirpath, _, filenames in os.walk(directory):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            total_size += os.path.getsize(filepath)
    return total_size

def generate_report(root_directory):
    report = {}
    for dirpath, dirnames, _ in os.walk(root_directory):
        directory_size = get_directory_size(dirpath)
        report[dirpath] = {
            'num_files': len(os.listdir(dirpath)),
            'num_directories': len(dirnames),
            'size': directory_size
        }
    return report

def print_report(report):
    for directory, data in report.items():
        print(f"Directory: {directory}")
        print(f"Number of files: {data['num_files']}")
        print(f"Number of directories: {data['num_directories']}")
        print(f"Total size: {data['size']} bytes\n")

# Example usage:
root_directory = "G:\Movies"
report = generate_report(root_directory)
print_report(report)
