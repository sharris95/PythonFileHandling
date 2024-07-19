#FileHandling

import os

def list_directory_contents(path):
    try:
        with os.scandir(path) as entries:
            for entry in entries:
                if entry.is_file():
                    print(f"File: {entry.name}")
                elif entry.is_dir():
                    print(f"Directory: {entry.name}")
    except FileNotFoundError:
        print(f"The directory {path} does not exist.")
    except PermissionError:
        print(f"Permission denied for accessing the directory {path}.")
if __name__ == "__main__":
    dir_path = input("Enter the directory path: ")
    list_directory_contents(dir_path)
