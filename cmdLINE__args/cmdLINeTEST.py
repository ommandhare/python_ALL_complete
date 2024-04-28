import sys


# sys.argv[0] is the script name, so arguments start from index 1
symbol_file = sys.argv[1]
operation_flag = sys.argv[2]
operation_flag=int(operation_flag)
print(operation_flag)

if operation_flag==2:
    print("HELLOOO")
