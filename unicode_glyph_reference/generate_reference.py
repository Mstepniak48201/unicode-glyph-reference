from pathlib import Path
from fontTools import ttLib

def main():
    file_name = input("File name: ")

    # Debug if input file exists
    if Path(file_name).is_file():
        print("The file exists")

    # Import the name of the input file to the output file, change extension, open new txt file.
    trimmed_file_name = trim_filename(file_name)
    output_file_name = add_file_extension(trimmed_file_name)
    output_file = open(output_file_name, "x")

    # Get reference to the font.
    font = ttLib.TTFont(file_name)

    # Get the cmap table (Python dict) from the font. Key: Value pairs are decimal_val: string_val
    font_cmap = font.getBestCmap()
    
    #convert keys in font_cmap dict to hex 
    hex_keys = []
    for key in font_cmap:
        hex_keys.append(hex(key))

    test_arr = ["Hello", "World", "append", "this", "value"]

    for el in test_arr:
        with open(output_file_name, "a") as f:
            f.write(el)

    
      

#Utility files

def trim_filename(file_name):
    output = []
    for char in file_name:
        if char == ".":
            break
        else:
            output.append(char)

    return "".join(output)

def add_file_extension(file_name):
    return "".join([file_name, ".txt"])
            
        

if __name__ == "__main__":
    main()
