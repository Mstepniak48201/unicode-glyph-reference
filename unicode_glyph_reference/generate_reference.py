from pathlib import Path
from fontTools import ttLib

def main():
    file_name = input("File name: ")

    # Trim the file name to add to the .txt file
    txt_output_name = trim_filename(file_name)

    print(txt_output_name)

    if Path(file_name).is_file():
        print("The file exists")

    # Get reference to the font.
    font = ttLib.TTFont(file_name)

    # Get the cmap table from the font.
    # After testing, I know that:
    # the value is a Python dict,
    # and that the key value pairs are decimal_value: string_value
    font_cmap = font.getBestCmap()
    
    #convert keys in font_cmap dict to hex
    hex_keys = []
    for key in font_cmap:
        hex_keys.append(hex(key))
        
    # print(hex_keys)
 
def trim_filename(file_name):
    output = []
    for char in file_name:
        if char == ".":
            break
        else:
            output.append(char)

    return "".join(output)
            
        

if __name__ == "__main__":
    main()
