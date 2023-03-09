import os

file_path = "/path/to/file.txt"

if os.path.exists(file_path):
    os.remove(file_path)
    print(f"File {file_path} deleted successfully")
else:
    print(f"File {file_path} does not exist")