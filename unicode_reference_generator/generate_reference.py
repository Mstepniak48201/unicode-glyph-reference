import os
from pathlib import Path
from fontTools import ttLib

def main():
    file_name = input("File name: ")

    # Initialize output directory
    initialize_output_directory("./output_text_files")


    with open("./output_text_files/test.txt", "a", encoding="utf-8") as f:
        f.write(f"hello output directory!\n") 


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

    # Get glyph names
    glyph_names = get_glyph_names(font_cmap)

    # Decimal Unicode Points
    decimal_u_points = get_decimal_u_points(font_cmap)

    # Format Hex Unicode Escape Codes
    hex_u_points = get_hex_u_points(decimal_u_points)

    with open(output_file_name, "a", encoding="utf-8") as f:
        f.write(f"Unicode Point  |  Glyph   |   Name\n") 
    
    for i in range(len(decimal_u_points)):
        with open(output_file_name, "a", encoding="utf-8") as f:
            f.write(f"{hex_u_points[i]}             {chr(decimal_u_points[i])}          {glyph_names[i]}\n")


#Utility functions

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

def get_glyph_names(cmap):
    result = []
    for key in cmap:
        result.append(cmap[key])
    return result

def get_decimal_u_points(cmap):
    result = []
    for key in cmap:
        result.append(key)
    return result
            
def get_hex_u_points(decimal_u_points):
    # Return array of formatted hex u points.
    hex_result = []

    # Iterate over array of decimal u points.
    for dec in decimal_u_points:
        # Construct an array to be joined as string.
        str_result = []
        hex_point = hex(dec)
        if dec < 65536:
            str_result.append("\\u00")
            str_result.append(hex_point[2:])
        else:
            str_result.append("\\U0000")
            str_result.append(hex_point[2:])
        hex_result.append("".join(str_result))

    return hex_result

def initialize_output_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)
        

if __name__ == "__main__":
    main()
