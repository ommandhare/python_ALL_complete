import sys

# Check if command-line arguments are provided
if len(sys.argv) < 2:
    print("Usage: python script_name.py arg1 arg2 ...")
    sys.exit(1)

# Access command-line arguments
script_name = sys.argv[0]
arguments = sys.argv[1:]

print("Script name:", script_name)
print("Arguments:", arguments)
