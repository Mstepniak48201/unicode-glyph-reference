from pathlib import Path
from fonttools import ttLib

def main():
    file_name = input("File name: ")
    print(file_name)

    if Path(file_name).is_file():
        print("The file exists")

if __name__ == "__main__":
    main()
