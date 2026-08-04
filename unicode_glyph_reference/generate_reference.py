from pathlib import Path
from fontTools import ttLib

def main():
    file_name = input("File name: ")
    print(file_name)

    if Path(file_name).is_file():
        print("The file exists")

    # Get reference to the font.
    font = ttLib.TTFont(file_name)

    # Get the cmap table from the font.
    font_cmap = font.getBestCmap()
    
    # print(font_cmap.keys())

    s = 0 

    for k in font_cmap.keys():
        s += 1

    print(s)

if __name__ == "__main__":
    main()
