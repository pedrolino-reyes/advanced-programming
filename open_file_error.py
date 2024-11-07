file_name = input("Enter File:")
try:
    print(open(file_name).read())
except FileNotFoundError:
    print(f"File not found: {file_name}")
